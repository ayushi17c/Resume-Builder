from flask import Blueprint, request, render_template, redirect, url_for, flash
from extensions import mongo
import bcrypt
from datetime import datetime

signup_bp = Blueprint("signup_bp", __name__)

@signup_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        existing_user = mongo.db.users.find_one({'email': email})
        if existing_user:
            flash("Email already exists.")
            return redirect(url_for('signup_bp.signup'))

        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        mongo.db.users.insert_one({
            'name': name,
            'email': email,
            'password': hashed_pw,
            'created_at': datetime.utcnow()
        })

        flash("Signup successful. Please login.")
        flash("Email already exists.", "error")

        return redirect(url_for('login_bp.login'))
    
    return render_template('signup.html')
