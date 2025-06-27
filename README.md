# 🚀 LangChain Beginner Projects

Welcome to the **LangChain Beginner Projects** repository! This series includes 5 practical projects that teach you how to use LangChain, LLMs, and related tools like Together API, Gradio, and Whisper — all from a beginner-friendly perspective.

Each project is organized in its own folder and can be launched from a central `main.py` Streamlit dashboard.

---

## 🧠 Tech Stack

- [LangChain](https://github.com/langchain-ai/langchain)
- [Together API](https://docs.together.ai/docs)
- [Streamlit](https://streamlit.io/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)
- [Gradio](https://www.gradio.app/)
- [Whisper](https://github.com/openai/whisper)

---

## 🗂️ Project Structure

```bash
langchain-beginner-projects/
│
├── main.py                  # Main dashboard to run projects
├── .env                     # API key goes here
├── requirements.txt
├── .gitignore
├── 1_chat_with_pdf/
├── 2_youtube_qa/
├── 3_ai_assistant/
├── 4_news_summarizer/
├── 5_voice_llm/
└── README.md
````

---

## ⚙️ How to Set Up

1. **Clone the repo**

   ```bash
   git clone https://github.com/talhasiddique7/LangChain-Beginner-Projects.git
   cd LangChain-Beginner-Projects
   ```

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the environment**

   * Windows:

     ```bash
     venv\Scripts\activate
     ```
   * macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **Set up your `.env` file**

   ```
   TOGETHER_API_KEY=your_api_key_here
   ```

6. **Run the main launcher**

   ```bash
   streamlit run main.py
   ```

---

## 📌 Project Descriptions

| Project                     | Folder                      | Description                                                                            | Key Features                        |
| --------------------------- | --------------------------- | -------------------------------------------------------------------------------------- | ----------------------------------- |
| **Chat with PDF**           | `1_chat_with_pdf/`   | Load PDF files, convert to embeddings, and chat with them using RAG.                   | LangChain, Vector Store, PDF Loader |
| **YouTube Q\&A**            | `2_youtube_qa/`      | Use video transcript to ask questions about any YouTube video.                         | Transcript Extractor, LLM Q\&A      |
| **AI Assistant with Tools** | `3_ai_assistant/`    | A personal assistant that can search the web, do math, and more using LangChain tools. | LangChain Agent, Tool Use           |
| **Daily News Summarizer**   | `4_news_summarizer/` | Automatically fetch and summarize today’s top headlines.                               | Web Scraping, Summarization         |
| **Voice Controlled LLM**    | `5_voice_llm/`       | Talk to your AI using microphone input and get LLM responses.                          | Whisper API, Gradio UI              |

---

## 🌐 APIs Used

* **Together API** for LLM responses
* **Whisper (OpenAI)** for voice transcription
* **News API / Web scraping** (in summarizer project)

---

## 🤝 Contributing

Feel free to fork this repo and improve the projects. Contributions are welcome!

---


## 📬 Contact

Made with ❤️ by **Talha Siddique**

