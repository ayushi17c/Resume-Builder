from flask import Flask
from flask import render_template
from extensions import mongo, login_manager, mail # Make sure 'mail' is in this import list
from bson.objectid import ObjectId
import bcrypt
import os
from dotenv import load_dotenv
import google.generativeai as genai
from routes.jd_tools import jd_bp
from auth.login import login_bp
from auth.signup import signup_bp
from auth.logout import logout_bp
from routes.dashboard import dash_bp
from routes.resume import resume_bp
from routes.generator import gen_bp
from auth.password import password_bp # You already have this import

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
app = Flask(__name__)
app.secret_key = "super_secret_key"
app.config["MONGO_URI"] = "mongodb://localhost:27017/resume_builder"

# Add this Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

mongo.init_app(app)
login_manager.login_view = 'login_bp.login'
login_manager.init_app(app)
mail.init_app(app) # CRUCIAL LINE: Initialize Flask-Mail with the app

from models.user import User

@login_manager.user_loader
def load_user(user_id):
    user_data = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    return User(user_data) if user_data else None

# Register blueprints
app.register_blueprint(dash_bp)
app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(jd_bp)
app.register_blueprint(resume_bp)
app.register_blueprint(gen_bp)
app.register_blueprint(password_bp) # Register the new password blueprint

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
