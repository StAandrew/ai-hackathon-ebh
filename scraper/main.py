import requests
import os
from dotenv import load_dotenv

load_dotenv()
FIRECRAWL_KEY = os.getenv('FIRECRAWL_KEY')
firecrawl_url = "https://api.firecrawl.dev/v1/scrape"

base_url = "https://www.rightmove.co.uk/property-to-rent/find.html?searchLocation=Kensington+And+Chelsea+%28Royal+Borough%29&useLocationIdentifier=true&locationIdentifier=REGION%5E61229&radius=0.0&_includeLetAgreed=on&includeLetAgreed=false"

payload = {
    "url": "<string>",
    "formats": ["markdown"],
    "onlyMainContent": True,
    "includeTags": ["<string>"],
    "excludeTags": ["<string>"],
    "headers": {},
    "waitFor": 123,
    "timeout": 123,
    "extract": {
        "schema": {},
        "systemPrompt": "<string>",
        "prompt": "<string>"
    },
    "actions": [
        {
            "type": "wait",
            "milliseconds": 2
        }
    ]
}
headers = {
    "Authorization": f"Bearer {FIRECRAWL_KEY}",
    "Content-Type": "application/json"
}

response = requests.request("POST", firecrawl_url, json=payload, headers=headers)

print(response.text)