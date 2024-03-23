# Import necessary libraries: aiohttp for asynchronous HTTP requests, asyncio for handling asynchronous tasks.
import aiohttp
import asyncio

# Define an asynchronous function to get data for a specific Pokemon based on its ID.
async def get_pokemon_data(pokemon_id):
    # Construct the URL for the PokeAPI with the specified Pokemon ID.
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    
    # Create an asynchronous HTTP session.
    async with aiohttp.ClientSession() as session:
        # Send a GET request to the specified URL.
        async with session.get(url) as response:
            # Await the response and parse it as JSON.
            data = await response.json()
            # Print the JSON data (this will be the data for the Pokemon).
            print(data)

# Define the main asynchronous function.
async def main():
    # Call the function to get data for Mew (Pokemon ID 151).
    await get_pokemon_data(151)

# Run the main function within the asyncio event loop.
asyncio.run(main())
