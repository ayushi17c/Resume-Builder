#🧑‍💼 Resume Builder
A modern, intelligent Resume Builder Web Application built using Python Flask.
This application enables users to create professional resumes tailored to job descriptions with the help of Google Gemini AI.

Designed for students, job seekers, and recruiters, it offers a smooth, secure, and efficient resume-building experience.


##🚀 Features
🔐 User Authentication
Secure Login & Signup with Email and Password
Forgot Password support with email verification
📧 Email notifications on login & signup
📝 Resume Generation
Create professional resumes tailored to job descriptions
AI-powered bullet point generation using Google Gemini API
Resume Preview before exporting
Export resumes as PDF


##🎨 Modern UI
Clean and responsive design with HTML, CSS, JavaScript
User-friendly interface for quick resume building
🗄️ Database & Storage
MongoDB integration for managing user accounts and session data


##📂 Tech Stack
Backend: Python Flask
Frontend: HTML5, CSS3, JavaScript
Database: MongoDB
AI Integration: Google Gemini API



##🔧 Setup Instructions

#Clone the repository
git clone https://github.com/ayushi17c/Resume-Builder.git
cd Resume-Builder


#Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate


#Install dependencies
pip install -r requirements.txt


#Set environment variables
Create a .env file and add:
GEMINI_API_KEY=your_api_key_here
MAIL_USERNAME=your_email_here
MAIL_PASSWORD=your_email_password


#Run the app
python app.py

##💡 Future Improvements
📑 Resume template selector with multiple design options
🔍 Auto keyword suggestions for ATS optimization
🌐 Multi-language resume support
📊 Resume analytics (track views/downloads)


#📫 Contact
Made with ❤️ by Ayushi
