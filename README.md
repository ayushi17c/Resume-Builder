#🧑‍💼 Resume Builder

A modern, intelligent Resume Builder web application built using Python Flask. It allows users to generate professional resumes tailored to job descriptions using AI (Google Gemini API).
This is designed with recruiters and job seekers in mind, offering a simple and efficient resume creation experience.

##🚀 Features

  🔐 Login & Signup using Name, Email and Password

  🔑 Forgot Password functionality with email verification

  📧 Email notifications on Login & Signup

  📝 Resume generation

  🧠 AI-powered bullet point generation using Google Gemini API

  👀 Resume preview before exporting

  🖨️ Export resume as PDF

  🖥️ Modern UI built with HTML, CSS, JavaScript

  📁 MongoDB integration for storing session/user data

##📂 Tech Stack

  Backend: Python Flask

  Frontend: HTML5, CSS3, JavaScript

  Database: MongoDB

  AI Integration: Google Gemini API

##🔧 Setup Instructions

1.Clone the repository

git clone https://github.com/ayushi17c/Resume-Builder.git
cd Resume-Builder


2.Create virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


3.Install dependencies

pip install -r requirements.txt


4.Set environment variables

Create a .env file and add:

GEMINI_API_KEY=your_api_key_here
MAIL_USERNAME=your_email_here
MAIL_PASSWORD=your_email_password


5.Run the app

python app.py


#📌 Note
This public repository has removed all sensitive API keys and secret configurations.
If you'd like to use Gemini AI integration, set your GEMINI_API_KEY securely in environment variables or a .env file (not pushed to GitHub).

##💡 Future Improvements

Resume template selector

Support for multiple resume exports

Auto keyword suggestions for ATS optimization

Multi-language resume support

#📫 Contact
Made with ❤️ by Ayushi
