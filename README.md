---
title: Insurance AI Assistant
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: streamlit
sdk_version: "1.32.2"
python_version: "3.10"
app_file: app.py
pinned: false
---

# 🤖 Insurance AI Assistant

An **AI-powered chatbot** that answers questions about **insurance policies, claims, and coverage** using **Retrieval Augmented Generation (RAG)**.

The assistant retrieves relevant information from an insurance knowledge base and generates accurate responses using a **Large Language Model (LLM)**.

---

# 🚀 Features

- 💬 AI chatbot for insurance queries  
- 🔎 Retrieval Augmented Generation (RAG) pipeline  
- ⚡ Fast responses using **Groq LLM**  
- 📚 Semantic search using **FAISS vector database**  
- 🧠 Context-aware responses using **LangChain**  
- 🌐 Interactive web interface built with **Streamlit**

---

# 🛠 Tech Stack

| Technology | Purpose |
|-------------|-------------|
| **Python** | Core programming language |
| **Streamlit** | Web application interface |
| **LangChain** | RAG pipeline orchestration |
| **FAISS** | Vector similarity search |
| **HuggingFace Embeddings** | Text embeddings for documents |
| **Groq API** | Fast LLM inference |

---

# 🧠 How It Works

1. Insurance documents are processed and converted into **vector embeddings**.
2. Embeddings are stored in a **FAISS vector database**.
3. When a user asks a question:
   - The system retrieves **relevant document chunks**.
   - These chunks are passed to the **LLM**.
4. The LLM generates an **accurate context-based response**.

---

# 📂 Project Structure

```
Insurance-AI-Assistant/
│
├── app.py               # Streamlit application
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── data/                # Insurance documents
└── vectorstore/         # FAISS vector database
```

---

# ▶️ Run Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/insurance-ai-assistant.git
cd insurance-ai-assistant
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set API Key

Add your **Groq API key** as an environment variable:

```bash
export GROQ_API_KEY="your_api_key_here"
```

or create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

### 4️⃣ Run the application

```bash
streamlit run app.py
```

---

# 📸 Example Use Cases

- What does health insurance cover?
- How do I file an insurance claim?
- What is the waiting period for health insurance?
- What documents are required for a claim?

---

# 📌 Future Improvements

- Support for **multiple insurance domains**
- **Voice-based queries**
- **Chat history memory**
- **Fine-tuned insurance LLM**

---

# 👨‍💻 Author

**Nishant Annalore**  
M.Sc Data Science  

---

# ⭐ If you like this project
