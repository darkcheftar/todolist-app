from pymongo import MongoClient



client = MongoClient("mongodb://localhost:27017/myFirstDatabase")


db = client.todo_app

collection_name = db["todos_app"]
