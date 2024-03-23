import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)

data = response.json()

# Extracting relevant information
timestamp = data['timestamp']
latitude = data['iss_position']['latitude']
longitude = data['iss_position']['longitude']

# Displaying the information
print(f"Timestamp: {timestamp}")
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")