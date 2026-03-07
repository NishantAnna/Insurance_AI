import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import pickle

# Load the chunks created in Step 1
with open("insurance_chunks.pkl", "rb") as f:
    chunks = pickle.load(f)

print("Chunks loaded:", len(chunks))

# Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Creating vector database...")

# Create FAISS vector DB
vector_db = FAISS.from_documents(chunks, embedding_model)

# Save vector DB
vector_db.save_local("insurance_vector_db")

print("Vector database created successfully!")