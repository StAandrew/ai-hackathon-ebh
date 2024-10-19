import json
import os
import sqlite3

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, Template
from openai import OpenAI

load_dotenv(".env")

llm_client = OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    api_key=os.environ.get("NEBIUS_API_KEY"),
)

file_loader = FileSystemLoader("/Users/stas_chi/Documents/Projects/Izba AI/izba-ai/backend/prompts")  # Specify the directory containing your template file
env = Environment(loader=file_loader)

def get_orchestrator_response(user_query: str) -> dict[str,str]:
    template = env.get_template('orchestrator.jinja2')
    # Render the template
    prompt = template.render(
        user_query = user_query
    )

    completion = llm_client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-405B-Instruct",
        messages=[
        {
            "role": "system",
            "content": prompt
        }
        ],
        temperature=0,
        max_tokens=1000,
        top_p=0.9
    )

    print(completion.choices[0].message.content)

    return {
        "debug_info": "",
        "llm_response": completion.choices[0].message.content
    }