import google.generativeai as genai
from utils.jd_parser import extract_keywords_from_jd

def score_resume_against_jd(resume_data, jd_text):
    jd_keywords = set(extract_keywords_from_jd(jd_text))
    
    fields = [resume_data.get(field, '') for field in ['summary', 'skills', 'experience', 'education']]
    combined_resume_text = ' '.join(fields).lower()
    
    matched_keywords = set()
    for word in jd_keywords:
        if word in combined_resume_text:
            matched_keywords.add(word)
    
    if len(jd_keywords) == 0:
        match_score = 0
    else:
        match_score = round(len(matched_keywords) / len(jd_keywords) * 100, 2)
        
    missed_keywords = list(jd_keywords - matched_keywords)
    
    return match_score, list(matched_keywords), missed_keywords



import re

def score_resume_semantically(resume_data, jd_text):
    model = genai.GenerativeModel('gemini-1.5-flash')

    resume_text = f"""
    Resume Details:
    Name: {resume_data.get('name', '')}
    Email: {resume_data.get('email', '')}
    Summary: {resume_data.get('summary', '')}
    Skills: {', '.join([item for sublist in [cat.get('items', []) for cat in resume_data.get('skills', [])] for item in sublist])}
    Experience: {resume_data.get('experience', '')}
    Education: {resume_data.get('education', '')}
    """

    prompt = (f"Analyze the following job description and resume. "
              "Provide a match score out of 100 based on how well the resume's skills and experience align with the job description. "
              "Then, list the key skills and experiences that **matched** and those that were **missed**. "
              "Use a structured format for the output: "
              "\nMatch Score: [Score]%"
              "\nMatched Keywords: [list of matched items]"
              "\nMissed Keywords: [list of missed items]"
              "\n\n---\n"
              "Job Description:\n"
              f"{jd_text}"
              "\n\n---\n"
              "Resume:\n"
              f"{resume_text}")

    try:
        response = model.generate_content(prompt)
        response_text = response.text.strip()
        
      
        score_match = re.search(r'Match Score:\s*(\d+)%', response_text)
        matched_match = re.search(r'Matched Keywords:\s*\[(.*?)\]', response_text, re.DOTALL)
        missed_match = re.search(r'Missed Keywords:\s*\[(.*?)\]', response_text, re.DOTALL)

        score = int(score_match.group(1)) if score_match else 0
        
        matched_keywords_str = matched_match.group(1) if matched_match else ''
        matched = [item.strip() for item in matched_keywords_str.split(',') if item.strip()]
        
       
        missed_keywords_str = missed_match.group(1) if missed_match else ''
        missed = [item.strip() for item in missed_keywords_str.split(',') if item.strip()]

       
        total_keywords = len(matched) + len(missed)
        if total_keywords > 0:
            recalculated_score = round((len(matched) / total_keywords) * 100, 2)
    
            if 0 <= score <= 100:
                final_score = score
            else:
                final_score = recalculated_score
        else:
            final_score = 0
            
        return final_score, matched, missed
    except Exception as e:
        print(f"Error with AI scoring: {e}")
        return 0, [], ["An error occurred with the AI service."]
