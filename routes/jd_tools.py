from flask import Blueprint, render_template, request, flash
from flask_login import current_user, login_required
from extensions import mongo
from utils.jd_parser import extract_keywords_from_jd
from utils.resume_scorer import score_resume_against_jd, score_resume_semantically

jd_bp = Blueprint("jd_bp", __name__)

@jd_bp.route("/jd-parser", methods=["GET", "POST"])
@login_required
def jd_parser():
    keywords = []
    if request.method == "POST":
        jd_text = request.form.get("jd_text")
        if jd_text:
            keywords = extract_keywords_from_jd(jd_text)
    return render_template("jd_parser.html", keywords=keywords)

@jd_bp.route("/resume-score", methods=["GET", "POST"])
@login_required
def jd_score():
    match_score = None
    matched = []
    missed = []
    
    resume_data = mongo.db.resumes.find_one({"user_id": current_user.id})

    if not resume_data:
        flash("Please create a resume first using the 'Resume Builder' page.")
        return render_template("jd_score.html")

    if request.method == "POST":
        jd_text = request.form.get("jd_text")
        
        if not jd_text:
            flash("Please paste a job description to score your resume.")
        else:
            try:
                match_score, matched, missed = score_resume_semantically(resume_data, jd_text)
            except Exception as e:
                flash(f"An error occurred while scoring your resume. Please try again later.")
                print(f"Error during resume scoring: {e}")
                
    return render_template("jd_score.html", score=match_score, matched=matched, missed=missed)
