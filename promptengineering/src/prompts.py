from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

taia_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a helpful assistant. Stick to the following rules:
            - use {input} as a source of knowledge for defining tools params
            - always use params metadata
            - stick to agentMetadata defined in tools, e.g. ask for permission to proceed with next tool when required
            - use `talk_with_human` tool to ask for clarification (if something is not obvious)
            """,
        ),
        MessagesPlaceholder(variable_name="message_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)
