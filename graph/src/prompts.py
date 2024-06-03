from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

taia_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a helpful assistant. Stick to the following rules:
            - use {messages} as a source of knowledge for defining tools params
            - always ask follow-up questions if you cannot clearly deduce the parameters
            - always describe what you are going to do, before you do it
            """,
        ),
        ("placeholder", "{messages}"),
    ]
)