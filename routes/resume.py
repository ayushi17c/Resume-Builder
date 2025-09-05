from flask import Blueprint, render_template, request, redirect, url_for, make_response, flash
from flask_login import login_required, current_user
from datetime import datetime
from extensions import mongo
from utils.pdf_generator import generate_pdf_from_html

resume_bp = Blueprint("resume_bp", __name__)

@resume_bp.route("/resume", methods=["GET", "POST"])
@login_required
def resume():
    if request.method == "POST":
        # Handle multiple experience entries
        job_titles = request.form.getlist('job_title')
        companies = request.form.getlist('company')
        experience_dates = request.form.getlist('experience_dates')
        experience_descriptions = request.form.getlist('experience_description')
        experience_list = []
        for i, title in enumerate(job_titles):
            if title.strip():
                experience_list.append({
                    'title': title,
                    'company': companies[i],
                    'dates': experience_dates[i],
                    'description': experience_descriptions[i]
                })

        # Handle multiple project entries
        project_titles = request.form.getlist('project_title')
        project_techs = request.form.getlist('project_tech')
        project_descriptions = request.form.getlist('project_description')
        project_list = []
        for i, title in enumerate(project_titles):
            if title.strip():
                project_list.append({
                    'title': title,
                    'tech': project_techs[i],
                    'description': project_descriptions[i]
                })

        # Handle multiple certifications
        certification_titles = request.form.getlist('certification_title')
        certification_orgs = request.form.getlist('certification_org')
        cert_list = []
        for i, title in enumerate(certification_titles):
            if title.strip():
                cert_list.append({
                    'title': title,
                    'organization': certification_orgs[i],
                })
        
        # Handle multiple custom links
        link_names = request.form.getlist('link_name')
        link_urls = request.form.getlist('link_url')
        links_list = []
        for i, name in enumerate(link_names):
            if name.strip() and link_urls[i].strip():
                links_list.append({
                    'name': name.strip(),
                    'url': link_urls[i].strip()
                })

        # Handle categorized skills
        skills = []
        technical_skills = request.form.get('technical_skills', '')
        soft_skills = request.form.get('soft_skills', '')
        
        if technical_skills:
            skills.append({'category': 'Technical Skills', 'items': [s.strip() for s in technical_skills.split(',') if s.strip()]})
        if soft_skills:
            skills.append({'category': 'Soft Skills', 'items': [s.strip() for s in soft_skills.split(',') if s.strip()]})
        
        resume_data = {
            'user_id': current_user.id,
            'name': request.form.get('name', ''),
            'email': request.form.get('email', ''),
            'phone': request.form.get('phone', ''),
            'summary': request.form.get('summary', ''),
            'education': {
                'degree': request.form.get('degree', ''),
                'university': request.form.get('university', ''),
                'graduation_date': request.form.get('graduation_date', '')
            },
            'skills': skills,
            'links': links_list,
            'certifications': cert_list,
            'experience': experience_list,
            'projects': project_list,
            'created_at': datetime.utcnow()
        }

        mongo.db.resumes.delete_many({'user_id': current_user.id})
        mongo.db.resumes.insert_one(resume_data)
        flash("Resume saved successfully!")
        return redirect(url_for("resume_bp.preview_resume"))
        
    else:
        resume_data = mongo.db.resumes.find_one({"user_id": current_user.id})
        return render_template("resume_form.html", data=resume_data if resume_data else {})

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
