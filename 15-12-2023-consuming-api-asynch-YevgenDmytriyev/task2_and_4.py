import aiohttp
import asyncio
import time

# Asynchronous function to get data for a specific Pokemon
# Function get_pokemon_data: This function takes a session and a Pokemon ID as parameters. 
# It makes an asynchronous GET request for the specified Pokemon and returns its name.

async def get_pokemon_data(session, pokemon_id):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    async with session.get(url) as response:
        data = await response.json()
        # Return the name of the Pokemon
        return data['name']

# Asynchronous main function to handle multiple requests

# Function main:

#   - Starts by recording the current time (start time).
#   - Opens an asynchronous HTTP session.
#   - Creates a list of tasks (tasks) where each task is a call to get_pokemon_data for 
# a different Pokemon ID (1 to 150).
#   - Uses await asyncio.gather(*tasks) to run all tasks concurrently. 
# This is where the power of asynchronous programming shines, as multiple requests are 
# handled simultaneously.
#   - Prints the name of each Pokemon.
#   - Measures the end time and prints the total duration taken to process all requests.

async def main():
    # Record the start time
    start_time = time.time()

    # Create an asynchronous HTTP session
    async with aiohttp.ClientSession() as session:
        # Create a list of tasks for each Pokemon ID
        tasks = [get_pokemon_data(session, pokemon_id) for pokemon_id in range(1, 151)]
        # Gather all tasks and wait for them to complete
        pokemon_names = await asyncio.gather(*tasks)

        # Print each Pokemon's name
        for name in pokemon_names:
            print(name)

    # Record the end time and calculate the total duration
    end_time = time.time()
    print(f"---{end_time - start_time} seconds---")

# Run the main function
asyncio.run(main())