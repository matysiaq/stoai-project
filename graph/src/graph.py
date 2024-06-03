from typing import Literal
import os

from graph.src.state import State
from graph.src.utils import gen_rand_str, create_tool_node_with_fallback
from graph.src.tools import sensitive_tools, safe_tools, sensitive_tool_names, wrapper
from graph.src.assistant import Assistant
from graph.src.prompts import taia_prompt

from IPython.display import Image, display

from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, StateGraph
from langgraph.prebuilt import tools_condition


def user_info(state: State):
    return {"user_info": gen_rand_str(12)}


def get_info(state: State):
    prompt = input("Human> ")
    messages = state["messages"] + [("user", prompt)]
    state = {**state, "messages": messages}
    return state


assistant_runnable = taia_prompt | wrapper.llm.bind_tools(
    safe_tools + sensitive_tools
)

builder = StateGraph(State)

builder.add_node("fetch_user_info", user_info)
builder.set_entry_point("fetch_user_info")
builder.add_node("assistant", Assistant(assistant_runnable))
builder.add_node("safe_tools", create_tool_node_with_fallback(safe_tools))
builder.add_node("sensitive_tools", create_tool_node_with_fallback(sensitive_tools))
builder.add_node("get_info", get_info)

builder.add_edge("fetch_user_info", "assistant")


def route_tools(state: State) -> Literal["safe_tools", "sensitive_tools", "get_info"]:
    next_node = tools_condition(state)
    # If no tools are invoked, return to the user
    if next_node == END:
        return "get_info"
    ai_message = state["messages"][-1]
    # This assumes single tool calls. To handle parallel tool calling, you'd want to
    # use an ANY condition
    first_tool_call = ai_message.tool_calls[0]
    if first_tool_call["name"] in sensitive_tool_names:
        return "sensitive_tools"
    return "safe_tools"


builder.add_conditional_edges(
    "assistant",
    route_tools,
)


def route_get_info(state: State) -> Literal["assistant", "__end__"]:
    condition_stop = False
    if condition_stop:
        return END

    return "assistant"


builder.add_conditional_edges(
    "get_info",
    route_get_info,
)

builder.add_edge("safe_tools", "assistant")
builder.add_edge("sensitive_tools", "assistant")

memory = SqliteSaver.from_conn_string(":memory:")

graph = builder.compile(
    checkpointer=memory,
    interrupt_before=["sensitive_tools"],
)


def display_graph():
    # Generate the graph PNG data
    png_data = graph.get_graph(xray=True).draw_mermaid_png()

    # Define the file name and path in the current directory
    file_name = "graph.png"
    file_path = os.path.join(os.getcwd(), file_name)

    # Save the PNG data to a file
    with open(file_path, "wb") as f:
        f.write(png_data)
