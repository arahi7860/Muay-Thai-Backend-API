import requests

url = 'https://muay-thai-backend-api-production.up.railway.app/techniques/{id}/'
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Replace {id} with the actual ID of the technique you want to delete
technique_id = 159
url = url.format(id=technique_id)

response = requests.delete(url, headers=headers)
print(response.status_code)
print(response.text)
