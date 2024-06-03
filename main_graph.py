from graph.src.graph import graph, display_graph
from graph.src.utils import print_event
from langchain_core.messages import ToolMessage

import uuid

if __name__ == "__main__":

    display_graph()
    thread_id = str(uuid.uuid4())

    config = {
        "configurable": {
            "thread_id": thread_id,
        }
    }

    _printed = set()

    for _ in range(5):
        print(f"[TAIA graph] I'm your Telco AI Assistant. What can I do for you?")
        prompt = input("Human> ")
        events = graph.stream(
            {"messages": ("user", prompt)}, config, stream_mode="values"
        )

        for event in events:
            print_event(event, _printed)

        snapshot = graph.get_state(config)
        while snapshot.next:
            user_input = input(
                "Do you approve of the above actions? Type 'y' to continue;"
                " otherwise, explain your requested changed.\nHuman> "
            )
            if (user_input.strip()).lower() == "y" or (user_input.strip()).lower() == "yes":
                result = graph.invoke(
                    None,
                    config,
                )
            else:
                # todo: not working well in some cases
                index = -1
                while len(event["messages"][-1].tool_calls) <= 0:
                    index = index - 1

                tool_call_id = event["messages"][index].tool_calls[0]["id"]

                result = graph.invoke(
                    {
                        "messages": [
                            ToolMessage(
                                tool_call_id=event["messages"][-1].tool_calls[0]["id"],
                                content=f"API call denied by user. Reasoning: '{user_input}'. "
                                        f"Continue assisting, accounting for the user's input.",
                            )
                        ]
                    },
                    config,
                )
            snapshot = graph.get_state(config)
