import requests
import json

def get_api_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None

def save_to_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# URLs for the APIs (Replace with actual API endpoints)
pokemon_api_url = 'https://pokeapi.co/api/v2/pokemon/?limit=15'
images_api_url = 'https://lorempokemon.fakerapi.it/pokemon/500/400'
places_api_url = 'https://fakerapi.it/api/v1/places?_quantity=15'

# Get data from APIs
pokemon_data = get_api_data(pokemon_api_url)
#images_data = get_api_data(images_api_url)
places_data = get_api_data(places_api_url)

# Save data to JSON files
save_to_json(pokemon_data, 'pokemon_data.json')
#save_to_json(images_api_url, 'images_data.json')
save_to_json(places_data, 'places_data.json')

# Create new dictionaries and print results
pokeLocations = []
for i in range(15):
    pokeLocation = {
        "pokemon": pokemon_data['results'][i]['name'],  # Assuming the API returns a list of Pokemon with a 'name' field
        "image": images_api_url,         # Assuming the API returns a list of images with a 'url' field
        "location": places_data['data'][i]              # Assuming the API returns a list of places with lat/long info
    }
    pokeLocations.append(pokeLocation)

    # Print formatted pokeLocation
    print(f"--------\nPokemon {i+1}\n--------")
    print(f"Name: {pokeLocation['pokemon']}")
    print(f"Image: {pokeLocation['image']}")
    print(f"Latitude: {pokeLocation['location']['latitude']}")
    print(f"Longitude: {pokeLocation['location']['longitude']}")
    print("--------")
