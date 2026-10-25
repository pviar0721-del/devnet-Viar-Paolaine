import random
import requests

pokemon_name = ['pikachu', 'mewtwo', 'charizard', 'bulbasaur', 'squirtle']

choice = random.choice(pokemon_name)
url = f"https://pokeapi.co/api/v2/pokemon/{choice}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    height = data["height"]
    weight = data["weight"]

    print("WHO'S THAT POKEMON!")
    print(f"Height: {height}")
    print(f"Weight: {weight}")
else:
    print("Could not find the Pokemon Information!")








