import requests

url = "http://api.open-notify.org/iss-now.json"

response = requests.get(url)
data = response.json()
lat = data['iss_position']['latitude']
lon = data['iss_position']['longitude']
print(response.status_code)
print(f"Current location is: lat{lat} lon{lon}")