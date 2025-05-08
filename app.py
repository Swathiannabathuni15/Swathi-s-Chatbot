import streamlit as st
import pyttsx3
import speech_recognition as sr
import json
import os
from gtts import gTTS

# Resume knowledge base
resume_data = {
    "name": "Annabathuni Swathi",
    "email": "annabathuniswathi@gmail.com",
    "phone": "7893903966",
    "linkedin": "https://www.linkedin.com/in/swathi-annabathuni-a13462230/",
    "education": [
        {
            "degree": "B.Tech in Artificial Intelligence and Machine Learning",
            "institute": "Vasireddy Venkatadri Institute of Technology",
            "year": "2021–2025",
            "cgpa": "8.4"
        },
        {   
            "qualification": "Intermediate",
            "institute": "Sri Chaitanya Junior College",
            "year": "2019–2021",
            "percentage": "94.5%"
        },
        {
            "qualification": "Secondary School",
            "institute": "Sri Chaitanya School",
            "year": "2018–2019",
            "grade": "10/10"
        }
    ],
    "skills": [
        "C", "Java", "Python", "Power BI", "Numpy", "Pandas", "Matplotlib",
        "MySQL", "SQLite", "Git", "GitHub", "HTML", "CSS", "JavaScript"
    ],
    "projects": [
        {
            "title": "Facial Emotional Recognition",
            "description": "Developed a CNN-based model with VGG architecture, achieving 65% accuracy on the FER dataset. Included data augmentation and hyperparameter tuning."
        },
        {
            "title": "Real-Time Attendance Management System",
            "description": "Used ArcFace, OpenCV, Streamlit, and SMTP for real-time facial recognition-based attendance with email alerts and dashboards."
        },
        {
            "title": "AI Agent using Playwright",
            "description": "Browser automation agent using Playwright and Google-based LLM integration for real-time web task execution."
        }
    ],
    "internships": [
        "Salesforce (Apex programming and Developer Console)",
        "Google AI/ML Virtual Internship (deep learning, LLMs)",
        "Cognifyz Technologies (data engineering)",
        "Be10x (AI tools workshop)",
        "Android App Development by APSSDC"
    ],
    "certifications": [
        "Generative AI", "Java Programming (NPTEL)", "ML (IBM)",
        "Deep Learning with Keras (IBM)", "AWS Cloud Foundations", "Prompt Engineering"
    ],
    "extracurriculars": [
        "Member of ACM Student Chapter at VVIT",
        "Hackathon participant",
        "Girl Wanna Code by Flipkart"
    ]
}

# Function to get response
def get_response(user_input):
    user_input = user_input.lower()
    if "name" in user_input:
        return f"My name is {resume_data['name']}."
    elif "email" in user_input:
        return f"You can contact me at {resume_data['email']}."
    elif "phone" in user_input or "number" in user_input:
        return f"My phone number is {resume_data['phone']}."
    elif "linkedin" in user_input:
        return f"Here is my LinkedIn profile: {resume_data['linkedin']}"
    elif "education" in user_input:
        return "I have completed: " + ", ".join([f"{e['degree']} from {e['institute']} ({e['year']})" if 'degree' in e else f"{e['qualification']} from {e['institute']} ({e['year']})" for e in resume_data['education']])
    elif "skills" in user_input:
        return "My skills include: " + ", ".join(resume_data['skills'])
    elif "projects" in user_input:
        return "Here are my projects:\n" + "\n".join([f"- {p['title']}: {p['description']}" for p in resume_data['projects']])
    elif "internship" in user_input:
        return "I've completed internships with: " + ", ".join(resume_data['internships'])
    elif "certification" in user_input:
        return "I have certifications in: " + ", ".join(resume_data['certifications'])
    elif "extra" in user_input:
        return "I participated in: " + ", ".join(resume_data['extracurriculars'])
    else:
        return "Sorry, I didn't understand that. You can ask about my skills, projects, education, or contact info."

# Streamlit UI
st.title("🎤 Chat with Swathi's Resume")

user_query = st.text_input("Ask me about Swathi:")
engine = pyttsx3.init()
if st.button("Get Response"):
    response = get_response(user_query)
    st.write(response)

    # Optional: Text-to-speech
    engine = pyttsx3.init()
    engine.say(response)
    engine.runAndWait()

