import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import ChatGroqChain
from portfolio import Portfolio
from utils import Clean_Text

def create_streamlit_app(chat_groq, porfolio, clean_text):
    st.title("📧 Cold Mail Generator")
    url_input = st.text_input("Enter the URL of the job posting", value="https://careers.nike.com/senior-analyst-fraud-analytics-qa-focused/job/R-63363")
    submit_button = st.button("Generate Cold Mail")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            porfolio.load_portfolio()
            jobs = chat_groq.extract_jobs(data)
            for job in jobs:
                skills = job.get("skills", [])
                links = porfolio.query_links(skills)
                email = chat_groq.create_email(job, links)
                st.code(email, language="markdown")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    chain = ChatGroqChain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide", page_title="Cold Mail Generator", page_icon="📧")
    create_streamlit_app(chain, portfolio, Clean_Text)