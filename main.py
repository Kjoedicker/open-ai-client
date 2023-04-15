#!/usr/local/bin/python3

from client import OpenAiClient
import sys
import dotenv
import os

try:
    dotenv.load_dotenv()

    question = " ".join(sys.argv[1:])
    
    open_api_key= os.getenv('OPEN_API_KEY')
    base_url = "https://api.openai.com/v1/completions"

    instance = OpenAiClient(base_url, open_api_key)
    answers = instance.ask(question)
    
    print(answers[0])
except IndexError:
    print("A question is required")
except Exception as err:
    print(f'Error instantiating OpenAI instance: {err}')
