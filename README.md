

🧠 LangChain PDF Chatbot using Groq & HuggingFace

A powerful LangChain-based Python application that allows you to ask questions about any PDF — even 500+ pages! It uses **Hugging Face Embeddings** for semantic understanding and **Groq's LLaMA 3 (70B)** for accurate, real-time answers.

---

## 📚 Features

- ✅ Read and process large PDFs (100–500+ pages)
- 🤖 Ask natural language questions about the document
- 🧠 Uses `HuggingFaceEmbeddings` for high-quality chunking and vector search
- ⚡ Powered by `Groq` LLM (`llama3-70b-8192`) for fast, smart responses
- 💬 CLI-based chat interface for lightweight usage
- 🛠️ Easy to configure with `.env` and local PDFs

---

## 📁 Project Structure

langproj/
│
├── app.py               # Main application script
├── .env                 # API keys stored securely
├── requirements.txt     # Dependencies
└── data/
└── sample.pdf       # Your input PDF file

---

Put your PDF inside the `data/` folder and rename it as `sample.pdf` (or change the filename in `app.py`).


❓ Ask a question (type 'exit' to quit): What is the objective of this report?
🧠 Answer: The objective of the report is to analyze...


## 🧰 Tech Stack

* [LangChain](https://github.com/langchain-ai/langchain)
* [Groq API](https://console.groq.com)
* [Hugging Face Transformers](https://huggingface.co/)
* [FAISS](https://github.com/facebookresearch/faiss)
* [Python Dotenv](https://github.com/theskumar/python-dotenv)


