# 🧑‍💼 Resume Builder

A modern, intelligent Resume Builder web application built using **Python Flask**. It allows users to generate professional resumes tailored to job descriptions using AI. 
This is designed with recruiters and job seekers in mind, offering a simple and efficient resume creation experience.

---

## 🚀 Features

- 🔐 Login using Name, Email and Password
- 📝 Resume generation
- 🧠 AI-powered bullet point generation using OpenAI API (now removed for public repo)
- 🖨️ Export resume as PDF
- 🖥️ Modern UI built with HTML, CSS, JavaScript
- 📁 MongoDB integration for storing session/user data

---

## 📂 Tech Stack

- **Backend:** Python Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** MongoDB
- **AI Integration:** OpenAI API (was used for bullet generation)

---


## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/ayushi17c/Resume-Builder.git
   cd Resume-Builder
   
Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install dependencies
pip install -r requirements.txt

Run the app
python app.py

📌 Note
This public repository has removed all sensitive API keys and secret configurations.
If you'd like to use OpenAI integration, set your OPENAI_API_KEY securely in environment variables or a .env file (not pushed to GitHub).

💡 Future Improvements
Resume template selector

Support for multiple resume exports

Auto keyword suggestions for ATS optimization


📫 Contact
Made with ❤️ by Ayushi

