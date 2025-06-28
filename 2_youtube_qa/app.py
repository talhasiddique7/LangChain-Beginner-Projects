import os
import hashlib
import streamlit as st
from dotenv import load_dotenv

from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.llms import Together
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA

from transcript_loader import get_video_transcript

# Load environment variables
load_dotenv()
# Set up Streamlit
st.set_page_config(page_title="YouTube Q&A", layout="wide")
st.title("🎥 YouTube Video Q&A - LangChain + Together API")

# Directory to store FAISS indexes
VECTOR_DIR = "vectorstores"
os.makedirs(VECTOR_DIR, exist_ok=True)

# Helper to generate unique hash from URL
def get_video_hash(url):
    return hashlib.md5(url.encode()).hexdigest()

# Streamlit input
video_url = st.text_input("🔗 Enter YouTube video URL:")

if video_url:
    try:
        with st.spinner("📄 Processing transcript..."):
            video_hash = get_video_hash(video_url)
            store_path = os.path.join(VECTOR_DIR, video_hash)

            embeddings = HuggingFaceEmbeddings()

            # Load or create FAISS store
            if os.path.exists(store_path):
                vectorstore = FAISS.load_local(store_path, embeddings, allow_dangerous_deserialization=True)
                st.success("✅ Loaded existing vector store from disk.")
            else:
                transcript = get_video_transcript(video_url)

                # Chunk transcript
                text_splitter = CharacterTextSplitter(
                    separator=" ",
                    chunk_size=1000,
                    chunk_overlap=100,
                    length_function=len,
                )
                texts = text_splitter.split_text(transcript)

                # Create and save FAISS
                vectorstore = FAISS.from_texts(texts, embeddings)
                vectorstore.save_local(store_path)
                st.success("📦 Transcript processed and stored locally.")

            # Setup LLM
            llm = Together(
                model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
                temperature=0.7,
                max_tokens=512,
            )

            # QA chain
            qa = RetrievalQA.from_chain_type(
                llm=llm,
                retriever=vectorstore.as_retriever(),
                return_source_documents=True,
            )

            # Ask question
            question = st.text_input("❓ Ask a question about the video:")
            if question:
                result = qa({"query": question})

                st.markdown("### 💡 Answer")
                st.write(result["result"])

                with st.expander("🧾 Source Transcript"):
                    for doc in result["source_documents"]:
                        st.write(doc.page_content[:300] + "...")

    except Exception as e:
        st.error(f"❌ Error: {str(e)}")
