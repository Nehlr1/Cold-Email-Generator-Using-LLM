import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

Groq_API_KEY = os.getenv("GROQ_API_KEY")
if not Groq_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it before running the application.")

class ChatGroqChain:
    def __init__(self):
        self.chat_groq =ChatGroq(api_key=Groq_API_KEY, temperature=0.0, model_name="llama-3.3-70b-versatile")
    
    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.chat_groq
        result = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            result = json_parser.parse(result.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse job.")
        return result if isinstance(result, list) else [result]
    
    def create_email(self, job, links):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Muhammad Ali, a Business Development Executive at Somikoron AI, an AI & Software Consulting company. 
            Somikoron AI specializes in creating tailored solutions that empower businesses to optimize processes, reduce costs, and scale efficiently through advanced automation and AI-driven tools. 
            Your task is to craft a compelling cold email to the client based on the provided job description, demonstrating how Somikoron AI's expertise aligns with their specific needs. 
            Highlight the most relevant accomplishments and projects from the following portfolio links with bullet points: {link_list}.
            Ensure the tone is professional, persuasive, and client-focused and avoid contractions. 
            Avoid any introductory remarks or preamble in the email.

            ### EMAIL (START DIRECTLY WITH THE CONTENT, NO PREAMBLE):
            """
        )


        chain_email = prompt_email | self.chat_groq
        result = chain_email.invoke(input={"job_description": str(job), "link_list": links})
        return result.content
    
if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))