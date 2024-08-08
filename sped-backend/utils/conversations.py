from langchain.agents import create_openai_tools_agent

def select_chat_agent(llm, tools, prompt):
    agent = create_openai_tools_agent(llm=llm, tools=tools, prompt=prompt)

    return agent
