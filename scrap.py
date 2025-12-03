"""import requests

url1 = ""
url = ""

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url, headers=headers)

#print(response.text[:500])

print(response.content)
"""

import requests
from bs4 import BeautifulSoup
import json
import re

url = "https://www.myntra.com/lipstick"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

#script_tag = soup.find("script", {"type": "application/ld+json"})

#data = json.loads(script_tag.string)
#print(data)
#products = data["itemListElement"]

#for item in products:
#    print(f"{item['position']}. {item['name']} → {item['url']}")

scripts = soup.find_all("script", {"type": "application/ld+json"})

data = None

for s in scripts:
    try:
        candidate = json.loads(s.string)
        if isinstance(candidate, dict) and candidate.get("@type") == "ItemList":
            data = candidate
            break
    except:
        continue

if data is None:
    raise Exception("ItemList JSON not found")

products = data["itemListElement"]

for p in products:
    name = p["name"]
    product_url = p["url"]

    # Extract product ID
    match = re.search(r'/(\d+)(/buy)?', product_url)
    product_id = match.group(1) if match else None

    print(f"{name} => {product_url} | Product ID: {product_id}")
