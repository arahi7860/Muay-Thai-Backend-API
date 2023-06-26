import requests

url = 'https://muay-thai-backend-api-production.up.railway.app/techniques/{id}/'
headers = {
    'Accept': 'application/json'
}

# Replace {id} with the actual ID of the technique you want to retrieve
technique_id = 162
url = url.format(id=technique_id)

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())
