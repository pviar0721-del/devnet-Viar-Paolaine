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
    ability = data["abilities"][0]["ability"]["name"]
    
    print("WHO'S THAT POKEMON!")
    print(f"Height: {height}")
    print(f"Weight: {weight}")
    print(f"Ability: {ability}")

    for attempt in range(3,0,-1):
        print(f"Remaining attempt is {attempt}/3")
        guess = input(f"Enter your answer:")

        if guess == choice:
            print(f"You got the CORRECT answer, Pokemon is {choice}!")
            break
        else: 
            print("Engk! Wrong Answer!")
    else:
        print("Game Over! No attempt left!")
        print(f"The Pokemon is {choice}!")
else:
    print("Could not find the Pokemon Information!")








