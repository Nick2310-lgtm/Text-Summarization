import streamlit as st
from summarizer import generate_summary

st.set_page_config(page_title="Text Summarizer", layout="centered")

st.title("📝 Text Summarization App")
st.markdown("Enter a long piece of text below, and this app will summarize it for you using a transformer model.")

user_input = st.text_area("Enter text to summarize:", height=300)

if st.button("Summarize"):
    if user_input.strip() != "":
        with st.spinner("Summarizing..."):
            try:
                summary = generate_summary(user_input)
                st.subheader("📌 Summary:")
                st.write(summary)
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("⚠️ Please enter some text.")
