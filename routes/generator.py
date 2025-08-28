from flask import Blueprint, request, render_template, jsonify
from utils.bullet_generator import generate_bullets_from_title

gen_bp = Blueprint('gen_bp', __name__)

@gen_bp.route('/bullet-generator', methods=['GET', 'POST'])
def bullet_generator():
    bullets = []
    if request.method == 'POST':
        # Get the job title from the form
        job_title = request.form.get('title')
        if job_title:
            bullets = generate_bullets_from_title(job_title)
    
    
    return render_template('generate_bullets.html', bullets=bullets)