from openai import OpenAI
import pandas as pd
import time
import os
from dotenv import load_dotenv

def generate_response(model="gpt-3.5-turbo"):
    load_dotenv()
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    client = OpenAI()
    prompt = "You will take a job application email as an input and return information about the job, which is these fields\n1. Position applied for (including any ID that may correspond to the job)\n2. Stage of the application  (Rejected, Accepted, Under Review, Unrelated)\n3. The company name\nIf the stage is not related, only return a JSON response with key stage and value Unrelated\nIf it is related, format the output as a JSON with the following keys: position, company, stage\nIf a certain element is not seen in the text, return an empty string for that element."
    messages = [{"role":"system","content":prompt}, {"role":"user","content":"Hi Karnika, Thank you for taking the time to apply to Software Engineer Intern and going through our hiring process. We really appreciate your interest in joining Johnson & Johnson. As you go through the process, we take the time to review your professional background and experience and make sure that they align with what’s needed for the role. Though your achievements are impressive, they didn’t exactly line up with what we’re looking for in this particular job. We want you to know that there are three main reasons as to why it might not have worked out and some have nothing to do with you"}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    print("ok", response.choices[0].message.content)
    return response.choices[0].message.content
generate_response()