import requests
from pymongo import MongoClient

# Conectarse a MongoDB (asegúrate de tener un servidor MongoDB en ejecución)
cliente_mongo = MongoClient('localhost', 27017)
db = cliente_mongo['pokeapi']
coleccion_pokemon = db['pokemons']

# Obtener datos de la PokeAPI para los primeros 150 Pokémon
url_pokeapi = 'https://pokeapi.co/api/v2/pokemon/?limit=150'
respuesta = requests.get(url_pokeapi)
datos_pokemons = respuesta.json()['results']

# Insertar los datos en la colección de MongoDB
for pokemon in datos_pokemons:
    nombre_pokemon = pokemon['name']
    url_pokemon = pokemon['url']

    # Obtener detalles del Pokémon
    detalle_respuesta = requests.get(url_pokemon)
    detalle_pokemon = detalle_respuesta.json()

    # Insertar en la colección de MongoDB
    coleccion_pokemon.insert_one({
        'nombre': nombre_pokemon,
        'detalles': detalle_pokemon
    })

print("Datos de los primeros 150 Pokémon insertados en MongoDB.")


"""
Ejemplos de consulta:

db.pokemons.findOne(
    {'nombre':'bulbasaur', 'detalles.id': 1 },
    { '_id': 0, 'nombre': 1, 'detalles.id': 1, 'detalles.stats': 1, 'detalles.abilities': 1 }
    )
"""