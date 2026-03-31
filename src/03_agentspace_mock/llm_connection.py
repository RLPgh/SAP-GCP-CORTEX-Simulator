import os
import google.generativeai as genai
from dotenv import load_dotenv

def configure_gemini():
    """Configure the Gemini API connection."""
    load_dotenv()
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
        
    genai.configure(api_key=api_key)
    # Return model instance
    model = genai.GenerativeModel('gemini-1.5-pro-latest')
    return model

if __name__ == "__main__":
    model = configure_gemini()
    print("Gemini model configured successfully.")
