import os
import streamlit as st
import time

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq


# ---------------- API KEY ---------------- #

os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]




# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="Insurance AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Insurance AI Assistant")
st.caption("Chat with an AI assistant about insurance policies, claims, and coverage.")


# ---------------- SIDEBAR ---------------- #

with st.sidebar:

    st.header("About")
    st.write(
        "This AI assistant answers questions related to insurance policies, claims, and coverage."
    )

    st.header("Example Questions")

    st.write("• What is claim settlement process?")
    st.write("• What documents are required for reimbursement?")
    st.write("• Does insurance cover accidents?")
    st.write("• What is waiting period in health insurance?")


# ---------------- LOAD MODELS ---------------- #

@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )


@st.cache_resource
def load_vector_db(_embeddings):
    return FAISS.load_local(
        "insurance_vector_db",
        _embeddings,
        allow_dangerous_deserialization=True
    )


@st.cache_resource
def load_llm():
    return ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.4
    )


embeddings = load_embeddings()
db = load_vector_db(embeddings)
retriever = db.as_retriever(search_kwargs={"k": 3})
llm = load_llm()


# ---------------- CHAT HISTORY ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# ---------------- USER INPUT ---------------- #

user_prompt = st.chat_input("Type your message...")


if user_prompt:

    st.chat_message("user").markdown(user_prompt)

    st.session_state.messages.append(
        {"role": "user", "content": user_prompt}
    )

    with st.spinner("Thinking..."):

        docs = retriever.invoke(user_prompt)

        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
You are a smart, friendly AI assistant like ChatGPT.

Your job is to give **clear, well-formatted answers**.

RESPONSE STYLE RULES:

1. If the user says greetings like:
   - hi
   - hello
   - hey

   Reply in a friendly conversational way.

2. If the user asks a question:
   - Give a **clear explanation**
   - Use **bullet points if helpful**
   - Use **numbered steps for processes**
   - Use **short paragraphs instead of long blocks**

3. Important information should be shown as:

• Bullet points  
or  
1. Numbered steps

4. Keep answers **clean, structured, and easy to read**.

5. If insurance information is available in the context, use it.

6. If the question is unrelated to insurance, still answer helpfully.


Insurance Document Context:
{context}


User Question:
{user_prompt}


Answer in a clear structured format:
"""

        response = llm.invoke(prompt).content


    # ---------------- STREAMING RESPONSE ---------------- #

    with st.chat_message("assistant"):

        placeholder = st.empty()
        full_response = ""

        words = response.split()

        for word in words:
            full_response += word + " "
            time.sleep(0.02)
            placeholder.markdown(full_response + "▌")

        placeholder.markdown(full_response)

    st.session_state.messages.append(
        {"role": "assistant", "content": full_response}
    )
