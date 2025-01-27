from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY"),
)

def ask_chatgpt(question):
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    
    return response.choices[0].message.content

question = "Qual é a temperatura média da cidade de porto alegre (RS) em fevereiro"

answare = ask_chatgpt(question)

print(answare)