# 🤖 Insurance AI Assistant

An AI chatbot that answers questions about **insurance policies, claims, and coverage** using **Retrieval Augmented Generation (RAG)**.

##  Features

* Chatbot for insurance-related queries
* Uses **LangChain + FAISS** for document retrieval
* **Groq LLM (Llama 3)** for fast responses
* Built with **Streamlit**

## 🛠 Tech Stack

* Python
* Streamlit
* LangChain
* FAISS
* HuggingFace Embeddings
* Groq API

## 📂 Project Structure

```
insurance-ai-chatbot/
│
├── app.py
├── requirements.txt
└── insurance_vector_db/
```

## ▶️ Run Locally

Install dependencies:

```
pip install -r requirements.txt
```

Run the app:

```
streamlit run app.py
```

##  API Key

Add your Groq API key:

```
GROQ_API_KEY="your_api_key"
```

##  Author

Nishant
