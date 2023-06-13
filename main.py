import requests
token = '7d77ef28e879abd16a6388894d4b6892'
host = 'https://pokemonbattle.me:9104'
response = requests.post(f'{host}/trainers/reg', json = {
    "trainer_token": token,
    "email": "5klblt@greencafe24.com",
    "password": "pkZwl6U1O9CxOIM3bRva"}, 

headers = {"Content-Type" : "application/json"})
print(response.text)

response_confirm = requests.post(f'{host}/trainers/confirm_email', json = {
    "trainer_token": token},

headers = {"Content-Type" : "application/json"})
print(response_confirm.text)

response_create = requests.post(f'{host}/pokemons', json = {
    "name": "Петрушка",
    "photo": "https://dolnikov.ru/pokemons/albums/007.png"},

headers = {"Content-Type" : "application/json",
"trainer_token": token})
print(response_create.text)

response_changes = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "13302",
    "name": "Марк"},
    headers = {"Content-Type" : "application/json",
"trainer_token": token})
print(response_changes.text)

response_add_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
     "pokemon_id": "13302"},
     headers = {"Content-Type" : "application/json",
"trainer_token": token})
print(response_add_pokeball.text)