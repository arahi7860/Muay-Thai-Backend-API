import requests

url = 'http://muay-thai-backend-api-production.up.railway.app/techniques/160'

response = requests.get(url)

print(response.status_code)
print(response.text)
