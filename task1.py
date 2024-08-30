# fetches the data for pikachu
#Then fetches the names and abilities and weight for 3 different pokemon
#displays the average weight



import requests
import json


#Task 2: Fetching Data from the Pokémon API


response=requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
json_data=response.text
pikachu_data=json.loads(json_data)
abilities = [ability['ability']['name'] for ability in pikachu_data['abilities']]

print(f'\nName: {pikachu_data["name"].capitalize()},  Abilities: {", ".join(abilities).replace("-", " ").title()}')
print()

#Task 3: Analyzing and Displaying Data for 3 different pokemon")
def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    json_data = response.text
    pokemon_data = json.loads(json_data)
    abilities = [ability['ability']['name'] for ability in pokemon_data['abilities']]
    weight = pokemon_data.get("weight")
    print(f'Name: {pokemon_data["name"].capitalize()}, Abilities: {", ".join(abilities).replace("-", " ").title()}, Weight: {weight}')
pokemon_list = ["pikachu", "bulbasaur", "charmander"]
for pokemon in pokemon_list:
   fetch_pokemon_data(pokemon)
   
print()
#Calculates the Average weight
pokemon_data_with_weight={}
def calculate_average_weight(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)
    json_data = response.text
    pokemon_data = json.loads(json_data)
    weight=pokemon_data.get("weight")
    return pokemon, weight 
    
   
pokemon_list = ["pikachu", "bulbasaur", "charmander"]
for pokemon in pokemon_list:
    pokemon_name,weight= calculate_average_weight(pokemon)
    pokemon_data_with_weight[pokemon_name]=weight
    
    
res = sum(pokemon_data_with_weight.values()) / len(pokemon_data_with_weight)
  
print("The averagde weight : " + str(res))