import json
import os
import sqlite3

from dotenv import load_dotenv
from jinja2 import Environment, FileSystemLoader, Template
from openai import OpenAI

load_dotenv(".env")

# Create a Template object
file_loader = FileSystemLoader("/Users/stas_chi/Documents/Projects/Izba AI/backend/prompts")  # Specify the directory containing your template file
env = Environment(loader=file_loader)
template = env.get_template('historical_data_to_sql.jinja2')

# Render the template
prompt = template.render(
    user_query = "What was the average price of detached houses in 2020?"
    # user_name="Lara",
    # topic="machine learning advancements",
    # curiosity="how reinforcement learning is evolving"
)

llm_client = OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    api_key=os.environ.get("NEBIUS_API_KEY"),
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

try:
    SQL_QUERY = json.loads(completion.choices[0].message.content)["SQL_QUERY"]
    print(SQL_QUERY)
except:
    print("Failed to load JSON from LLM output")


# Step 1: Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('/Users/stas_chi/Documents/Projects/Izba AI/backend/databases/price_paid_data.db')  # Replace with your database file

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Run a SELECT query to fetch data
cursor.execute(SQL_QUERY)
results = cursor.fetchall()

# Step 4: Process and print the results
for row in results:
    print(row)

# Step 5: Close the connection
conn.close()