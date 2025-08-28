import google.generativeai as genai

def generate_bullets_from_title(title: str) -> list[str]:
    """
    This function uses the Google Gemini AI model to generate professional resume bullet points.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')

        prompt = (f"Write a concise and professional resume summary for a {title} role. "
          "The summary should be 3-4 sentences long, highlight key skills and qualifications, "
          "and be tailored to attract recruiters in the field. "
          "Provide only the summary paragraph, without any extra conversation or formatting.")

        response = model.generate_content(prompt)
        
        
        bullets = [bullet.strip() for bullet in response.text.split('\n') if bullet.strip()]
        
        if not bullets:
            return [f"Could not generate bullets for '{title}'. Try a different title."]
            
        return bullets
        
    except Exception as e:
        print(f"Error generating bullets with AI: {e}")
        return [f"Could not generate bullets for '{title}'. An error occurred with the AI service."]