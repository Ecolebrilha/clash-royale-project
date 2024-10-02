from pymongo import MongoClient

connection_string = "mongodb+srv://fernandobastosleite7:fernandinho123.@clash-royale-cluster.4yanq.mongodb.net/?retryWrites=true&w=majority&appName=clash-royale-cluster"

client = MongoClient(connection_string)

db = client.clashroyale
collection = db.cards

card = {
    "name": "Goblins",
    "id": 1,
    "rarity": "Common",
    "maxLevel": 13,
    "elixirCost": 2,
    "maxEvolutionLevel": 3
}

collection.insert_one(card)
print("Documento inserido:", card)
