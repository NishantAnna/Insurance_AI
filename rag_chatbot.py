from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM

print("Loading embedding model...")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Loading FAISS database...")

db = FAISS.load_local(
    "insurance_vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(search_kwargs={"k":3})

print("Loading local LLM...")

llm = OllamaLLM(model="mistral")

print("\nInsurance RAG Assistant Ready")
print("--------------------------------")

while True:

    query = input("\nAsk Question: ")

    if query.lower() in ["exit", "quit"]:
        break

    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are an insurance assistant.

    Use the context below to answer the question.

    Context:
    {context}

    Question:
    {query}

    Answer clearly.
    """

    response = llm.invoke(prompt)

    print("\nAnswer:\n")
    print(response)