# openrouter_client.py

import requests
import os
from dotenv import load_dotenv
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

'''
def generate_linkedin_message(job):
    prompt = f"""
            Write a short and professional LinkedIn outreach message tailored for this role:

            Job Title: {job.get('title', 'N/A')}
            Company: {job.get('company', 'N/A')}
            Link: {job.get('link', 'N/A')}

            Tone: friendly and concise (and too long message and not too short message) and perosnal
            Goal: express interest, highlight quick learning & AI enthusiasm, request a short call/chat
              """
'''  

def generate_linkedin_message(job):
    prompt = f"""
            You are a professional AI communication assistant. Your task is to write a concise, high-impact LinkedIn connection message tailored to a specific internship opportunity.

Details:

Job Title: {job.get('title', 'N/A')}

Company: {job.get('company', 'N/A')}

Job Link: {job.get('link', 'N/A')}

Instructions:

Hook: Start with a warm, personalized greeting that references the job title or company.

Value: Highlight interest in the role, emphasize your quick adaptability, and passion for AI.

Tone: Polished, human, respectful — avoid generic or mechanical language.

Length: Must be under 300 characters.

Call to Action: End with a polite ask for a brief chat or intro call.

Constraints:

Do not use markdown formatting.

Keep it readable, naturally flowing, and precise — no filler or fluff.
"""
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        #"model": "google/gemini-2.0-flash-exp:free",
        "model" : "deepseek/deepseek-chat-v3-0324:free",
        #"model" : "deepseek/deepseek-r1-0528:free",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        print(f"❌ OpenRouter Error: {response.status_code}, {response.text}")
        return "Could not generate message at this time."
