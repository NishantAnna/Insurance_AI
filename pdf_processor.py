import os
import pickle
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Folder containing PDFs
PDF_FOLDER = "data"

all_documents = []

print("Loading PDFs...")

for file in os.listdir(PDF_FOLDER):
    if file.endswith(".pdf"):
        path = os.path.join(PDF_FOLDER, file)

        loader = PyPDFLoader(path)
        documents = loader.load()

        # Add file name in metadata
        for doc in documents:
            doc.metadata["source_file"] = file

        all_documents.extend(documents)

print("Total pages loaded:", len(all_documents))

# Text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(all_documents)

print("Total chunks created:", len(chunks))

# SAVE chunks for next step
with open("insurance_chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("Chunks saved as insurance_chunks.pkl")

# Show example chunk
print("\n------ SAMPLE CHUNK ------\n")
print(chunks[0].page_content)
print("\nMetadata:", chunks[0].metadata)