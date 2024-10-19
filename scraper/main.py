import requests
import os
import sqlite3
from pydantic import BaseModel, Field
from typing import List
from firecrawl import FirecrawlApp
from dotenv import load_dotenv

load_dotenv()
FIRECRAWL_API_KEY = os.getenv('FIRECRAWL_API_KEY')
firecrawl_url = "https://api.firecrawl.dev/v1/scrape"

search_url = "https://www.rightmove.co.uk/property-to-rent/find.html?searchLocation=Kensington+And+Chelsea+%28Royal+Borough%29&useLocationIdentifier=true&locationIdentifier=REGION%5E61229&radius=0.0&_includeLetAgreed=on&includeLetAgreed=false"

app = FirecrawlApp(api_key=FIRECRAWL_API_KEY)


class PropertySchema(BaseModel):
  property_id: str = Field(..., alias="property_id")
  property_url: str = Field(..., alias="property_url")
  property_title: str = Field(..., alias="property_title")
  property_description: str = Field(..., alias="property_description")
  property_address: str = Field(..., alias="property_address")
  property_postcode_short: str = Field(..., alias="property_postcode_short")
  property_postcode_full: str = Field(..., alias="property_postcode_full")
  property_price_per_month: str = Field(..., alias="property_price_per_month")


# Define a schema for the full extraction, which includes a list of properties
class ListingsSchema(BaseModel):
  listings: List[PropertySchema]

data = app.scrape_url(search_url, {
  'formats': ['extract'],
  'extract': {
    'schema': ListingsSchema.model_json_schema(),
  }
})
for listing in data["extract"]["listings"]:
    print(listing)
