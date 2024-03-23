# Python APIs - Consume REST APIs

## Asynchronous REST Requests

Asynchronous code has increasingly become a mainstay of Python development. Let's use the ```aiohttp``` library to take advantage of this for making asynchronous HTTP requests, which is one of the most common use cases for non-blocking code.

In this exercise, you will:
1. Install aiohttp
2. Make simple GET requests with aiohttp
3. Make a large number of requests with aiohttp
4. Compare speed between synchronous and asynchronous requests

We're going to use the [Pokemon API](https://pokeapi.co/docs/v2) as an example.
Here is also a aiohttp [quickstart guide](https://docs.aiohttp.org/en/stable/client_quickstart.html) to get you up and running fast with the required methods and syntax.

### 1. Install aiohttp

````
> pip3 install aiohttp
````

### 2. Make simple GET requests with aiohttp

Let's start off by making a single ```GET``` request using ```aiohttp```, to demonstrate how the keywords async and await work.

**TASKs:** S
Start by trying to get the data associated with the legendary 151st Pokemon, Mew.

### 3. Make a large number of requests with aiohttp

Making a single asynchronous HTTP request is great because you can let the event loop work on other tasks instead of blocking the entire thread while waiting for a response. But this functionality truly shines when trying to make a larger number of requests.  

**TASKs:** 
- Demonstrate this by performing the same request as before, but for all 150 of the original Pokemon.

***HINT: Take the previous request code and put it in a loop, updating which Pokemon's data is being requested and using await for each request***

-  Also measure how much time the whole process takes. 

- Print your data to something like the following to your terminal:

````
aerodactyl
snorlax
articuno
zapdos
moltres
dratini
dragonair
mewtwo
---8.10269960403442 seconds---
````

### 4. Compare speed between synchronous and asynchronous requests

Async requests made with ```aiohttp``` perform much faster than synchronous  HTTP client libraries like [Requests](https://docs.python-requests.org/en/latest/).
Let's compare how well the two perform.

**TASKs:** 
- Print the first 150 Pokemon as before, but using the [Requests](https://docs.python-requests.org/en/latest/) library. Also calculate and print the time as before.
- Compare the speed of responses for the two libraries.
