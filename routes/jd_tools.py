from flask import Blueprint, render_template, request
from utils.jd_parser import extract_keywords_from_jd
from utils.resume_scorer import score_resume_against_jd
from flask_login import current_user
from extensions import mongo


jd_bp = Blueprint("jd_bp", __name__)

@jd_bp.route("/jd-parser", methods=["GET", "POST"])
def jd_parser():
    keywords = []
    if request.method == "POST":
        jd_text = request.form.get("jd_text")
        if jd_text:
            keywords = extract_keywords_from_jd(jd_text)
    return render_template("jd_parser.html", keywords=keywords)

@jd_bp.route("/jd-score", methods=["GET", "POST"])
def jd_score():
    match_score = None
    matched = []
    missed = []
    if request.method == "POST":
        jd_text = request.form.get("jd_text")
        resume_data = mongo.db.resumes.find_one({"user_id": current_user.id})
        if jd_text and resume_data:
            match_score, matched, missed = score_resume_against_jd(resume_data, jd_text)
    return render_template("jd_score.html", score=match_score, matched=matched, missed=missed)