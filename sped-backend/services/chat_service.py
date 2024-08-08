import os
from dotenv import load_dotenv
from utils.conversations import select_chat_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor
from langchain.tools import tool

# Loading environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Defining custom tool
@tool
def search() -> int:
    """search for SPED information"""
    return 

tools = [search]

# Defining the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that can guide parents with labyrinth of SPED system."),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "Hello, how are you doing?"),
        ("ai", "I'm doing well, how can I help you regarding SPED systems today?"),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ]
)

# Defining the model and agent
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
agent = select_chat_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

# Function to invoke agent
async def handle_chat_query(query: str):
    response = agent_executor.invoke({"input": query})
    return response
