# Candidate Matching Recommendation System

### Overview
This project implements a recommendation system that matches candidates to job openings using machine learning techniques. It analyzes resumes to predict the most suitable job category for each candidate, helping streamline the hiring process.

### Features
Data Preprocessing: Cleans and preprocesses resume text to prepare it for analysis.
TF-IDF Vectorization: Converts text data into numerical format suitable for machine learning models.
Model Training: Utilizes classifiers such as K-Nearest Neighbors for multi-class classification.
User Interface: A Streamlit app allows users to upload resumes and receive job category predictions.

### Working
Data Cleaning: Removes noise, stopwords, and lemmatizes text for better analysis.
TF-IDF Transformation: Converts resumes into a format that highlights important words while reducing the impact of common words.
Model Training: Trains a machine learning model on historical hiring data to classify resumes into job categories.
Prediction: Uses the trained model to predict the most suitable job category for a given resume.

### Project Structure
cleaning_text.py: Contains functions for text preprocessing.
model_training.py: Loads data, preprocesses resumes, trains models, and saves them.
app.py: A Streamlit application that provides an interface for resume screening.

### Conclusion
The candidate matching system enhances the recruitment process by efficiently matching candidates to relevant job openings based on their resumes. This project showcases the power of NLP and machine learning in human resources applications.