from langchain_core.runnables import Runnable, RunnableConfig
from graph.src.state import State


class Assistant:
    def __init__(self, runnable: Runnable):
        self.runnable = runnable

    def __call__(self, state: State, config: RunnableConfig):

        result = self.runnable.invoke(state)

        self._print_msg(result)

        return {"messages": result}

    @staticmethod
    def _print_msg(result: any):
        if len(result.content) > 0:
            print("================================== Ai Message ==================================")
            print(result.content)

        if "tool_calls" in result.additional_kwargs:
            print("================================== Tool Calls ==================================")
            for index in range(len(result.additional_kwargs["tool_calls"])):
                print("-\t", result.additional_kwargs["tool_calls"][index])
