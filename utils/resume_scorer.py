from utils.jd_parser import extract_keywords_from_jd

def score_resume_against_jd(resume_data, jd_text):
    jd_keywords = set(extract_keywords_from_jd(jd_text))
    resume_keywords = set()

    # Combine all resume fields into a single string
    fields = [resume_data.get(field, '') for field in ['summary', 'skills', 'experience', 'education']]
    combined_resume_text = ' '.join(fields).lower()

    for word in jd_keywords:
        if word in combined_resume_text:
            resume_keywords.add(word)

    match_score = round(len(resume_keywords) / len(jd_keywords) * 100, 2) if jd_keywords else 0
    return match_score, list(resume_keywords), list(jd_keywords - resume_keywords)