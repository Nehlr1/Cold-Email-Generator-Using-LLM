import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class ChatGroqChain:
    def __init__(self):
        self.chat_groq =ChatGroq(temperature=0.0, model_name="llama-3.3-70b-versatile")
    
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
            You are Muhammad Ali, a business development executive at Somikoron AI. Somikoron AI is an AI & Software Consulting company dedicated to facilitating
            the seamless integration of business processes through automated tools. 
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
            process optimization, cost reduction, and heightened overall efficiency. 
            Your job is to write a cold email to the client regarding the job mentioned above describing the capability of Somikoron AI 
            in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase Somikoron AI's portfolio: {link_list}
            Remember you are Muhammad Ali, BDE at Somikoron AI. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):

            """
        )

        chain_email = prompt_email | self.chat_groq
        result = chain_email.invoke(input={"job_description": str(job), "link_list": links})
        return result.content
    
if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))