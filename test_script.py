import requests

url = 'https://muay-thai-backend-api-production.up.railway.app/techniques/'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
data = {
    "name": "Test Technique 6",
    "description": "I am tired",
    "img": "https://example.com/test.gif",
    "category": "Punches"
}

response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.json())
