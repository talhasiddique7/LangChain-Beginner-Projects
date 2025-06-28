import os
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.llms import Together
from langchain.chains import RetrievalQA

# Load API key
load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

st.set_page_config(page_title="Chat with your PDF", layout="wide")
st.title("📄 Chat with Your PDF - LangChain + Together API")

# Upload PDF
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Load and split PDF
    loader = PyPDFLoader("temp.pdf")
    pages = loader.load_and_split()

    st.success(f"Loaded {len(pages)} pages from the PDF.")

    # Create embeddings
    embeddings = HuggingFaceEmbeddings()
    db = FAISS.from_documents(pages, embeddings)

    # Set up Together LLM
    llm = Together(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        temperature=0.7,
        max_tokens=512,
    )

    # Set up QA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=db.as_retriever(),
        return_source_documents=True
    )

    # Chat interface
    query = st.text_input("Ask a question about the PDF:")

    if query:
        result = qa_chain({"query": query})
        st.markdown("### 📌 Answer")
        st.write(result["result"])

        with st.expander("📚 Source Documents"):
            for doc in result["source_documents"]:
                st.write(doc.page_content[:300] + "...")
