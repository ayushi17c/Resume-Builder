from flask import Blueprint, render_template, request, redirect, url_for, make_response
from flask_login import login_required
from flask_login import current_user
from datetime import datetime
from extensions import mongo
from utils.pdf_generator import generate_pdf_from_html

resume_bp = Blueprint("resume_bp", __name__)

@resume_bp.route("/resume", methods=["GET", "POST"])
@login_required
def resume():
    if request.method == "POST":
       resume_data = {
        'user_id': current_user.id,
        'name': request.form['name'],
        'email': request.form['email'],
        'phone': request.form['phone'],
        'summary': request.form['summary'],
        'experience': request.form['experience'],
        'education':request.form['education'],
        'skills': request.form['skills'].split(','),
        'created_at': datetime.utcnow()
          }

# Optional: Overwrite previous resume instead of creating duplicates
       mongo.db.resumes.delete_many({'user_id': current_user.id})
       mongo.db.resumes.insert_one(resume_data)
       return redirect(url_for("resume_bp.preview_resume"))
    return render_template("resume_form.html")


@resume_bp.route("/resume/preview")
@login_required
def preview_resume():
    resume_data = mongo.db.resumes.find_one({"user_id": current_user.id})
    return render_template("resume_preview.html", data=resume_data)

@resume_bp.route("/resume/download")
@login_required
def download_resume():
    resume_data = mongo.db.resumes.find_one({"user_id": current_user.id})
    html = render_template("resume_final.html", data=resume_data)
    pdf = generate_pdf_from_html(html)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = "attachment; filename=resume.pdf"
    return response


