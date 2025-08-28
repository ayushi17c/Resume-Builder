# routes/generator.py

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
            # Call the AI utility function to get the bullets
            bullets = generate_bullets_from_title(job_title)
    
    # Render the HTML template, passing the generated bullets
    return render_template('generate_bullets.html', bullets=bullets)

# Optional: You can keep the API endpoint if you have a separate use for it
# but it seems redundant based on your current project structure.
# @gen_bp.route('/api/bullet-generator', methods=['POST'])
# def bullet_generator_api():
#     job_title = request.json.get('title')
#     if job_title:
#         bullets = generate_bullets_from_title(job_title)
#         return jsonify({'bullets': bullets})
#     return jsonify({'error': 'No title provided'}), 400







#from flask import Blueprint, request, jsonify

#gen_bp = Blueprint('gen_bp', __name__)

#@gen_bp.route('/api/bullet-generator', methods=['POST'])
#def bullet_generator():
   # jd_text = request.json.get('jd')
    # Use your AI model here to generate bullets
   # bullets = ["Generated bullet 1", "Generated bullet 2"]  # Replace with actual AI output
   # return jsonify({'bullets': bullets})