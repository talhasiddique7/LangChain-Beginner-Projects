import streamlit as st
import subprocess

st.title("🧠 LangChain Beginner Projects")
st.header("Author: Talha Siddique")
st.subheader("🚀 Launch Your Project")
st.write("Select a project to launch:")

projects = {
    "Chat with PDF": "1_chat_with_pdf/app.py",
    "YouTube Q&A": "2_youtube_qa/app.py",
    "AI Assistant with Tools": "3_ai_assistant/app.py",
    "Daily News Summarizer": "4_news_summarizer/app.py",
    "Voice Controlled LLM": "5_voice_llm/app.py"
}

choice = st.selectbox("📁 Choose a project", list(projects.keys()))

if st.button("🚀 Launch Project"):
    st.success(f"Launching {choice}...")
    subprocess.run(["streamlit", "run", projects[choice]])
