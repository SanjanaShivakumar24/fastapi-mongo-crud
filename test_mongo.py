from pymongo import MongoClient

uri = "mongodb+srv://sanjanashivakumar:k9dweZUoYmMAazIx@cluster0.d0cecdx.mongodb.net/sample_mflix?retryWrites=true&w=majority&authSource=admin"

try:
    client = MongoClient(uri)
    print("Connected successfully!")
    print("Databases:", client.list_database_names())
except Exception as e:
    print("Connection failed:", e)
