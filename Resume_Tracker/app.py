import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pypdf
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("API"))

def get_response(input_text):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input_text)
    return response.text

def in_file_read(file):
    reader = pypdf.PdfReader(file)
    text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text

input_prompt = '''
Think that you are an Experienced HR, who has 10 years of Experience in Hiring people.
now looking at the following data Extract me name, Education, Work Experiece, Skills and 
match candidate resumes with job descriptions based on the extracted information.
resume: {text}
description: {jd}

I want the response one below the other which follow the following structure.
{{"Name": '',
'Education':'',
'Work Experience': '',
'Skills': '',
"JD match":"%",
"Matching": ['yes','no],
"Missing Keywords":[],
"Profile Summary":""}}
follow the same procedure first name then below education below work experience and so on and all the letters should be bold
'''

st.title("Smart ATS")
st.text("Improve your Resume Score")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader('Upload your resume', type='pdf', help='Please upload a PDF file')
submit = st.button('Submit')

if submit:
    if uploaded_file is not None:
        resume_text = in_file_read(uploaded_file)
        formatted_input = input_prompt.format(text=resume_text, jd=jd)
        response = get_response(formatted_input)
        st.subheader(response)
    else:
        st.error("Please upload a resume.")
