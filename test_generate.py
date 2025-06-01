import requests

url = "http://localhost:5000/generate"
payload = {"prompt": "resilience"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
