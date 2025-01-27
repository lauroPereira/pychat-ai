import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def ask_chatgpt(question):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    
    return response.choices[0].message.content

question = "Qual é a temperatura média da cidade de porto alegre (RS) em fevereiro"

answare = ask_chatgpt(question)

print(answare)