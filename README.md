# 🎥 YouTube QnA Assistant (RAG Pipeline)

A lightweight Retrieval-Augmented Generation (RAG) application built with **LangChain** and **Streamlit** that allows users to paste a YouTube video URL and ask specific questions about its content based directly on the video's transcript.


## 🚀 Features
- **Automated Extraction**: Pulls transcripts directly from YouTube videos using `YoutubeLoader`.
- **Semantic Search**: Chunks text using `RecursiveCharacterTextSplitter` and indexes them into a local **FAISS** vector database.
- **Accurate Grounding**: Uses Google's **Gemini 2.5 Flash** model with custom prompt templates to prevent hallucinations and ensure answers are concise.
- **Interactive UI**: Built with a clean, fast **Streamlit** sidebar layout for easy user inputs.

---

## 🛠️ Tech Stack
- **Framework**: LangChain (LCEL)
- **Frontend**: Streamlit
- **LLM**: Google Gemini 2.5 Flash 
- **Embeddings**: Google Multimodal Embeddings 
- **Vector Database**: FAISS (Facebook AI Similarity Search)
- **Environment & Package Manager**: `uv` (by Astral)

---

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd YOUR_REPO_NAME
   ```

2. **Set up your environment variables:**
   Create a `.env` file in the root directory and add your Google AI Studio API key:
   ```env
   GOOGLE_API_KEY="your_gemini_api_key_here"
   ```

3. **Install dependencies and run via `uv`:**
   ```bash
   # uv will automatically handle virtual environment setup and install all packages
   uv run streamlit run main.py
   ```

---

## 💡 How It Works
1. **Load**: `YoutubeLoader` fetches the raw transcript string of the specified video.
2. **Chunk**: The transcript is divided into overlapping blocks of 1000 characters to retain semantic context.
3. **Embed & Store**: Texts are converted into vectors using Gemini Embeddings and stored in an in-memory FAISS database.
4. **Retrieve**: When a query is made, FAISS performs a similarity search to fetch the top 4 matching blocks.
5. **Generate**: The retrieved chunks are formatted into a prompt context, and Gemini generates a concise string response.
