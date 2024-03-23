import requests
import time

def get_pokemon_data(pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response = requests.get(url)
    data = response.json()
    return data['name']

def main():
    start_time = time.time()

    for pokemon_id in range(1, 151):
        name = get_pokemon_data(pokemon_id)
        print(name)

    end_time = time.time()
    print(f"---{end_time - start_time} seconds---")

if __name__ == "__main__":
    main()