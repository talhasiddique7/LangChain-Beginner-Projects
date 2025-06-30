import os
import streamlit as st
from dotenv import load_dotenv

from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.tools import TavilySearchResults
from langchain.tools import tool
from langchain_community.llms import Together

# ====== Load API Keys from .env ======
load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Required for Together API to work inside LangChain
os.environ["TOGETHER_API_KEY"] = TOGETHER_API_KEY

# ====== Initialize Together LLM ======
llm = Together(
    model="lgai/exaone-3-5-32b-instruct",
    temperature=0.7,
    max_tokens=512
)

# ====== Tool 1: Tavily Web Search Tool ======
search_tool = TavilySearchResults(api_key=TAVILY_API_KEY)

# ====== Tool 2: Simple Calculator ======
@tool
def calculator(expression: str) -> str:
    """Evaluate a basic math expression like '5+5' or 'sqrt(16)'."""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error: {e}"

# ====== Combine Tools ======
tools = [
    Tool(
        name="web-search",
        func=search_tool.run,
        description="Search the web for up-to-date information"
    ),
    Tool(
        name="calculator",
        func=calculator,
        description="Useful for solving basic math expressions"
    )
]

# ====== Initialize Agent ======
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False
)

# ====== Streamlit UI ======
st.set_page_config(page_title="🧠 AI Assistant", layout="centered")
st.title("🧠 AI Assistant using LangChain + Together API")

st.markdown("""
Ask me anything!  
- 🔍 I can search the web  
- ➗ Solve math  
- 🧠 Use reasoning with LangChain tools
""")

query = st.text_input("📝 Enter your question:")

if query:
    with st.spinner("🤔 Thinking..."):
        try:
            response = agent.run(query)
            st.success("✅ Here's what I found:")
            st.markdown(response)
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
