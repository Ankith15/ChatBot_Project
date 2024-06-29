# JobDetails Assistant

The JobDetails Assistant is a conversational AI designed to provide information and guidance to candidates regarding job openings within a company. It utilizes natural language processing (NLP) techniques and integrates advanced AI models for efficient interaction.

### Features
PDF Text Extraction: Extracts text from PDF documents containing job descriptions.
Text Chunking: Splits extracted text into manageable chunks for processing.
Semantic Embeddings: Generates semantic embeddings using Google Generative AI for text representation.
Vector Storage: Stores text embeddings in a vector store using FAISS for fast similarity search.
Question Answering: Answers candidate queries based on job details using a pre-trained conversational AI model.
Interactive Interface: Provides a user-friendly chat interface using Streamlit for seamless interaction.

### Usage
Upload Job Description PDFs: Ensure PDF files containing job descriptions (des.pdf in this case) are available in the project directory.
Interact with the Chatbot: Enter queries related to job openings. The chatbot will provide responses based on the information extracted from the PDF documents.

### Project Structure
app.py: Main application file containing the Streamlit app setup and user interaction logic.
utils.py: Helper functions for PDF text extraction, text chunking, vector storage, and question answering.
models/: Directory containing trained AI models and embeddings.

### Technologies Used
Streamlit: Framework for building interactive web applications.
PyPDF2: Library for reading and extracting text from PDF files.
LangChain: Python library for text processing, including text splitting and semantic embeddings.
Google Generative AI: Provides advanced embeddings for semantic understanding.
FAISS: Efficient library for similarity search and vector storage.