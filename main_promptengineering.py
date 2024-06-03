from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.runnables.history import RunnableWithMessageHistory

from langchain_community.chat_message_histories import ChatMessageHistory

from promptengineering.src.utils import gen_rand_str
from promptengineering.src.tools import tools, wrapper
from promptengineering.src.prompts import taia_prompt


if __name__ == "__main__":

    agent = create_tool_calling_agent(llm=wrapper.llm, tools=tools, prompt=taia_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True,
                                   return_intermediate_steps=True)

    message_history = ChatMessageHistory()

    agent_with_chat_history = RunnableWithMessageHistory(
        agent_executor,
        lambda session_id: message_history,
        input_messages_key="input",
        history_messages_key="message_history",
    )

    # print(f"[TAIA promptengineering] {wrapper.hello_msg()}")
    print(f"[TAIA promptengineering] I'm your Telco AI Assistant. What can I do for you?")
    for _ in range(5):
        query = input("[Human] > ")

        out = agent_with_chat_history.invoke(
            {"input": f"{query}", "message_history": f"{message_history}"},
            config={"configurable": {"session_id": f"{gen_rand_str(16)}"}},
        )

        print(f"[TAIA promptengineering] {out['output']}")
        message_history.messages.append(
            SystemMessage(f"Intermediate steps: {out['intermediate_steps']}")
        )

    print("\n[MESSAGE HISTORY]\n")
    print(message_history)

