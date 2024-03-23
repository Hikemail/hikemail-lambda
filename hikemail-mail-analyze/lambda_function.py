from openai import OpenAI
import pandas as pd
import time
import os
from dotenv import load_dotenv
import json

def generate_response(file_dict):
    # Get the API key from the .env file.
    load_dotenv()
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    # Implicitly links API key to the restAPI.
    client = OpenAI()

    # Generates the response
    model="gpt-3.5-turbo"
    prompt = "You will take a job application email as an input and return information about the job, which is these fields\n1. Position applied for (including any ID that may correspond to the job)\n2. Stage of the application  (Rejected, Accepted, Under Review, Unrelated)\n3. The company name\nIf the stage is not related, only return a JSON response with key stage and value Unrelated\nIf it is related, format the output as a JSON with the following keys: position, company, stage\nIf a certain element is not seen in the text, return an empty string for that element."
    messages = [{"role":"system","content":prompt}, {"role":"user","content":file_dict["file"]}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    # Converts the content of the output to a python dictionary.
    return json.loads(response.choices[0].message.content)

def lambda_handler(event, context):
     # Get the unique ID of the message. This corresponds to the name of the file
    # in S3.
    message_id = event['Records'][0]['ses']['mail']['messageId']
    print(f"Received message ID {message_id}")

    # Retrieve the file from the S3 bucket.
    file_dict = get_message_from_s3(message_id)

    # Send the message body to OpenAI restapi to generate response.
    response = generate_response(file_dict)
    print(response)