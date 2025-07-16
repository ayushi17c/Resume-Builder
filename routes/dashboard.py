from flask import Blueprint, render_template
from flask_login import login_required, current_user
from extensions import mongo

dash_bp = Blueprint("dash_bp", __name__)

@dash_bp.route('/dashboard')
@login_required
def dashboard():
    resume_count = mongo.db.resumes.count_documents({'user_id': current_user.id})
    return render_template("dashboard.html", email=current_user.email, resume_count=resume_count)
