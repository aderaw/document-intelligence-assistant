import streamlit as st
from pdf_reader import extract_text
from extractor import extract_info

st.set_page_config(page_title="Document Intelligence Assistant", layout="wide")

st.title("📄 Document Intelligence Assistant")
st.write("Upload a PDF and extract structured information using AI")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF uploaded successfully!")

    # Step 1: Extract text
    text = extract_text(uploaded_file)

    st.subheader("📄 Extracted Text (Preview)")
    st.text(text[:1500])

    # Step 2: Run AI extraction
    if st.button("Extract Information"):
        with st.spinner("Analyzing document with Gemini AI..."):
            result = extract_info(text)

        st.subheader("📊 Extracted Structured Data")
        st.code(result, language="json")