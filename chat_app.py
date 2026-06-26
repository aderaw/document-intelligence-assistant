import streamlit as st
from pdf_reader import extract_text
from chat_rag import ask_pdf

st.set_page_config(
    page_title="Document Intelligence Assistant",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("💬 Chat with Your PDF (AI Assistant)")

# Session memory
if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Upload PDF
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    st.success("PDF uploaded successfully!")

    # Extract text once
    if st.session_state.pdf_text is None:
        st.session_state.pdf_text = extract_text(uploaded_file)

    st.info("You can now ask questions about the document 👇")

# Chat input
question = st.text_input("Ask a question about the PDF")

if question and st.session_state.pdf_text:
    with st.spinner("Thinking... 🤖"):
        answer = ask_pdf(st.session_state.pdf_text, question)

    # Save chat history
    st.session_state.chat_history.append((question, answer))

# Show chat history
for q, a in reversed(st.session_state.chat_history):
    st.markdown("### 🧑 You")
    st.write(q)

    st.markdown("### 🤖 AI")
    st.write(a)

    st.divider()