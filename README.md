# Cold Email Generator

## Overview
Cold Email Generator is a Streamlit web application that generates personalized cold emails for job postings. It leverages AI (via Groq's LLM) to extract job details from a provided job posting URL, matches relevant skills with your portfolio, and crafts a compelling cold email tailored to the opportunity.

## Features
- **Job Posting Scraper:** Enter a job posting URL to extract job details (role, experience, skills, description).
- **Portfolio Matching:** Matches your portfolio projects/links to the required skills.
- **AI-Powered Email Generation:** Uses Groq's LLM to generate a professional, persuasive cold email.
- **Easy-to-Use UI:** Simple Streamlit interface for quick email generation.

## Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/Nehlr1/Cold-Email-Generator-Using-LLM
cd streamlit_app
```

### 2. Install Dependencies
Install required Python packages:
```
pip install -r requirements.txt
```

**Main dependencies:**
- streamlit
- langchain
- langchain_groq
- chromadb
- pandas
- python-dotenv

### 3. Prepare Portfolio Data
- Place your portfolio CSV file at `company portfolio data/my_portfolio.csv`.
- The CSV should have at least two columns: `Techstack` and `Links`.

### 4. Set Environment Variables
Create a `.env` file in the project root with your Groq API key:
```
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the App
```
streamlit run app.py
```

## Usage
1. Enter the URL of a job posting in the input field.
2. Click **Generate Cold Mail**.
3. The app will display a tailored cold email based on the job description and your portfolio.

## File Structure
- `app.py` - Main Streamlit app.
- `chains.py` - Handles job extraction and email generation using Groq LLM.
- `portfolio.py` - Loads and queries your portfolio data.
- `utils.py` - Utility functions (e.g., text cleaning).
- `company portfolio data/my_portfolio.csv` - Your portfolio data.
- `vectorstore/` - ChromaDB vector store for portfolio search.

## Notes
- Ensure your Groq API key is valid and has sufficient quota.
- The app is designed for English-language job postings.
- For best results, keep your portfolio CSV up to date and relevant.

## License
MIT License

## Author
Muhammad Ali (Somikoron AI)
