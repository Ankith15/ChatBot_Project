# Smart ATS (Applicant Tracking System)

Smart ATS is an intelligent system designed to parse and analyze resumes, extract key information, and match candidates with job descriptions using advanced AI techniques.

### Project Overview
The project utilizes machine learning and natural language processing to automate the resume screening process and enhance recruitment efficiency. Key features include:

Resume Parsing: Extracts essential details such as name, education, work experience, and skills from uploaded resumes.
Job Description Matching: Matches candidate resumes with job descriptions based on the extracted information.
Intelligent Response Generation: Uses Google Generative AI to generate structured responses for evaluating resume compatibility with job requirements.
    
### Technologies Used
Streamlit: Framework for building interactive web applications.
PyPDF2: Library for reading and extracting text from PDF files.
Google Generative AI: Provides advanced natural language generation capabilities.
Python dotenv: Loads environment variables from a .env file for API configuration.

### Usage
Upload Resume: Upload a PDF file containing a candidate's resume.
Enter Job Description: Paste or type the job description to compare against the uploaded resume.
Generate Analysis: Click the "Submit" button to analyze the resume and see the extracted information and match results.

### Project Structure
app.py: Main application file containing the Streamlit app setup and user interaction logic.
utils.py: Helper functions for PDF text extraction and API interaction.
models/: Directory for storing trained models and data related to resume parsing and matching.