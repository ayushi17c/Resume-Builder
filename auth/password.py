from flask import Blueprint, request, render_template, redirect, url_for, flash
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from extensions import mongo, mail
import bcrypt
from bson.objectid import ObjectId


s = URLSafeTimedSerializer('ThisIsASecretKey')

password_bp = Blueprint("password_bp", __name__)

@password_bp.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        user_data = mongo.db.users.find_one({'email': email})

        if user_data:
            token = s.dumps(str(user_data['_id']), salt='password-reset-salt')
            msg = Message("Password Reset Request",
                          sender="your_email@gmail.com",
                          recipients=[email])
            link = url_for('password_bp.reset_with_token', token=token, _external=True)
            msg.body = f"Your password reset link is: {link}"
            mail.send(msg)
            flash("A password reset link has been sent to your email.")
        else:
            flash("Email not found. Please try again.")

        return redirect(url_for('login_bp.login'))
    return render_template('forgot_password.html')

@password_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_with_token(token):
    try:
        user_id = s.loads(token, salt='password-reset-salt', max_age=3600)  # Token expires in 1 hour
    except:
        flash("The password reset link is invalid or has expired.")
        return redirect(url_for('login_bp.login'))

    if request.method == 'POST':
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            flash("Passwords do not match.")
            return render_template('reset_password.html', token=token)

        hashed_pw = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        mongo.db.users.update_one({'_id': ObjectId(user_id)}, {'$set': {'password': hashed_pw}})

        flash("Your password has been reset successfully. Please log in.")
        return redirect(url_for('login_bp.login'))

    return render_template('reset_password.html', token=token)