import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
# ---------------------------------------------------
# STEP 1: DEFINE PATH WHERE YOUR PDFs ARE STORED
# ---------------------------------------------------
DATA_PATH = "data"

# Store all extracted documents
all_documents = []

# ---------------------------------------------------
# STEP 2: LOAD ALL PDF FILES
# ---------------------------------------------------
for filename in os.listdir(DATA_PATH):

    if filename.endswith(".pdf"):

        file_path = os.path.join(DATA_PATH, filename)

        print(f"Loading: {filename}")

        loader = PyPDFLoader(file_path)

        documents = loader.load()

        # Add metadata (important for RAG later)
        for doc in documents:
            doc.metadata["source_file"] = filename

        all_documents.extend(documents)

print("\nTotal pages loaded:", len(all_documents))


# ---------------------------------------------------
# STEP 3: SPLIT TEXT INTO SMALL CHUNKS
# ---------------------------------------------------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,      # characters per chunk
    chunk_overlap=200     # overlapping text
)

chunks = text_splitter.split_documents(all_documents)

print("Total chunks created:", len(chunks))


# ---------------------------------------------------
# STEP 4: SHOW SAMPLE OUTPUT
# ---------------------------------------------------
print("\n------------ SAMPLE CHUNK ------------\n")

print(chunks[0].page_content[:500])

print("\nMetadata:", chunks[0].metadata)