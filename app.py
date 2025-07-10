import streamlit as st
from doc_parser import load_document
from rag_engine import build_vectorstore, answer_question
from summarizer import summarize_text

st.set_page_config(page_title="DocuGenie", page_icon="📄")
st.title("📄 DocuGenie - Your AI Document Assistant")

uploaded_file = st.file_uploader("Upload your document", type=["pdf", "docx", "txt"])
question = st.text_input("Ask a question about the document:")

if uploaded_file:
    text = load_document(uploaded_file)
    vectorstore = build_vectorstore(text)

    if question:
        answer = answer_question(vectorstore, question)
        st.markdown("### Answer")
        st.write(answer)

    if st.button("Summarize"):
        summary = summarize_text(text)
        st.markdown("### Summary")
        st.write(summary)
