import google.generativeai as genai
from utils.jd_parser import extract_keywords_from_jd

# -----------------
# BRUTE-FORCE SOLUTION (Keyword Matching)
# -----------------
def score_resume_against_jd(resume_data, jd_text):
    """
    Calculates a match score based on a simple keyword presence check.
    """
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


# OPTIMAL SOLUTION (Semantic Matching with AI)

def score_resume_semantically(resume_data, jd_text):
    """
    Calculates a more advanced match score using a generative AI model.
    """
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    
    resume_text = f"""
    Resume Details:
    Name: {resume_data.get('name')}
    Email: {resume_data.get('email')}
    Summary: {resume_data.get('summary')}
    Skills: {', '.join(resume_data.get('skills', []))}
    Experience: {resume_data.get('experience')}
    Education: {resume_data.get('education')}
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
        
        
        score_line = next((line for line in response_text.split('\n') if "Match Score:" in line), "Match Score: 0%")
        matched_line = next((line for line in response_text.split('\n') if "Matched Keywords:" in line), "Matched Keywords: ")
        missed_line = next((line for line in response_text.split('\n') if "Missed Keywords:" in line), "Missed Keywords: ")
        
        score_str = score_line.split(':')[1].strip().replace('%', '')
        try:
            score = int(score_str)
        except ValueError:
            score = 0
            
        matched = [item.strip() for item in matched_line.split(':')[1].split(',') if item.strip()]
        missed = [item.strip() for item in missed_line.split(':')[1].split(',') if item.strip()]

        return score, matched, missed
    except Exception as e:
        print(f"Error with AI scoring: {e}")
        return 0, [], ["An error occurred with the AI service."]