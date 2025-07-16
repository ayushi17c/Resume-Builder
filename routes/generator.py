from flask import Blueprint, request, render_template
from flask_login import login_required
from utils.bullet_generator import generate_bullets_from_title

gen_bp = Blueprint("gen_bp", __name__)

@gen_bp.route("/generate-bullets", methods=["GET", "POST"])
@login_required
def generate_bullets():
    bullets = []
    if request.method == "POST":
        title = request.form.get("title")
        if title:
            bullets = generate_bullets_from_title(title)
    return render_template("generate_bullets.html", bullets=bullets)