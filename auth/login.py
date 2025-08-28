from flask import Blueprint, request, render_template, redirect, url_for, flash
from flask_login import login_user
from extensions import mongo
from models.user import User
import bcrypt
from flask_mail import Message
from extensions import mail

login_bp = Blueprint("login_bp", __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')
        user_data = mongo.db.users.find_one({'email': email})
        
        if user_data and bcrypt.checkpw(password, user_data['password']):
            # --- Email Sending Logic for Login ---
            msg = Message("Login Notification",
                          sender="your_app_email@gmail.com", # Change to your app's email
                          recipients=[email])
            msg.body = "This is a notification that your account has been logged into."
            try:
                mail.send(msg)
            except Exception as e:
                print(f"Failed to send login email: {e}")
            # --- End of Email Sending Logic ---

            login_user(User(user_data))
            return redirect(url_for('dash_bp.dashboard'))
        else:
            flash("Invalid credentials")
            
    return render_template('login.html')