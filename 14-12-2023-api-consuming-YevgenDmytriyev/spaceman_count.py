import requests

url = "http://api.open-notify.org/astros.json"

response = requests.get(url)
data = response.json()
number = data['number']
print(response.status_code)
print(f"Currently, there are: {number} people in space")
