# FastAPI MongoDB Todo List

## Prerequisites

1. FastAPI basics
2. Python installed 
3. Mongodb Community server installed


## Install Dependencies

1. fastAPI
2. uvicorn
3. pymongo

```shell
$ pip install fastapi uvicorn pymongo pymongo[srv]
```

## Edit database.py

create a file called database.py and add the following content inside of it

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/mydb")

db = client.todo_app

collection_name = db["todos_app"]
```

**Note: the `"mongodb://localhost:27017/mydb**"` is optional since be default MongoClient will connect to this port and route.**

We may use Atlas or an online mongoDB platform, the the URL to the cluster in place to the argument used in the instantiation on the MongoDB client


## Run the server

```bash
$ uvicorn main:app
```
And App starts at http://127.0.0.1:8000 

You can explore api at `http://127.0.0.1:8000/docs` with swagger ui.