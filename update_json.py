import requests

url = 'https://muay-thai-backend-api-production.up.railway.app/techniques/{id}'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Replace {id} with the actual ID of the technique you want to update
technique_id = 160
url = url.format(id=technique_id)

data = {
    "name": "Roronoa Zoro",  # Updated name
    "description": "I am tired",
    "img": "https://example.com/test.gif",
    "category": "Punches"
}

response = requests.put(url, json=data, headers=headers)
print(response.status_code)
print(response.text)
