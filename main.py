from fastapi import FastAPI
from pydantic import BaseModel
import pymongo
from pymongo import MongoClient
import random
from bson.objectid import ObjectId

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()

# 데이터 모델 정의
class User(BaseModel):
    id: str
    name: str
    email: str
    
class UserData(BaseModel):
    data_id: str
    user_id: str
    fact:str
    response:str
    title:str
    painter:str
    image:Image
    

def convert_objectid(data):
    if isinstance(data, list):
        return [{**item, "_id": str(item["_id"])} for item in data if "_id" in item]
    elif isinstance(data, dict):
        data["_id"] = str(data["_id"]) if "_id" in data else None
        return data
    return data
# 기본 루트
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# GET 요청 처리
@app.get("/items/{item}")
def read_item(item: str):
    try:
        uri = "mongodb+srv://jihoon9835:wlgns9835@cluster0.xh3ds.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        client = MongoClient(uri)

        database = client["jihoon9835"]
        collection = database["image_info"]

        if item == "all":
            result = list(collection.find({}))
            result = convert_objectid(result)
        elif item == "random":
            results = list(collection.find({}))
            results = convert_objectid(results)
            result = random.choice(results)
        else:
            results = list(collection.find({"image":item}))
            if len(results)==0:
                result = None
            else:
                results = convert_objectid(results)
                result = results[0]

        # start example code here

        # end example code here

        client.close()

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)
    return {"data": result}


@app.get("/tag/")
def read_tags(tag: str):
    try:
        uri = "mongodb+srv://jihoon9835:wlgns9835@cluster0.xh3ds.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        client = MongoClient(uri)

        database = client["jihoon9835"]
        collection = database["image_tag"]

        if tag == "all":
            result = list(collection.find({}))
            result = convert_objectid(result)
        elif tag == "random":
            results = list(collection.find({}))
            results = convert_objectid(results)
            result = random.choice(results)
        else:
            results = list(collection.find({"tag":tag}))
            if len(results)==0:
                result = None
            else:
                results = convert_objectid(results)
                result = results[0]

        # start example code here

        # end example code here

        client.close()

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)
    return {"data": result}

@app.get("/user")
def read_all_user():
    try:
        uri = "mongodb+srv://jihoon9835:wlgns9835@cluster0.xh3ds.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        client = MongoClient(uri)

        database = client["jihoon9835"]
        collection = database["user_info"]
        result = list(collection.find({}))
        result = convert_objectid(result)
        client.close()

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)
    return {"data": result}

@app.get("/user/{user}")
def read_user(user_id: str):
    try:
        uri = "mongodb+srv://jihoon9835:wlgns9835@cluster0.xh3ds.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        client = MongoClient(uri)

        database = client["jihoon9835"]
        collection = database["user_info"]
        try:
            user_id = ObjectId(user_id)
        except:
            print("Invalid ObjectId")
        result = collection.find_one({"_id":user_id})
        result = convert_objectid(result)
        client.close()

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)
    return {"data": result}

@app.post("/user/")
def create_user(user: User):
    try:
        uri = "mongodb+srv://jihoon9835:wlgns9835@cluster0.xh3ds.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        client = MongoClient(uri)

        database = client["jihoon9835"]
        collection = database["user_info"]
        user_id = user.id
        user_name = user.name
        user_email = user.email
        result = collection.insert_one({"_id":user_id,"name": user_name, "email": user_email})
        client.close()
    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)
    return {"id": str(result.inserted_id), "data": user}



@app.get("/user_data")
def read_all_user_data():
    try:
        uri = "mongodb+srv://jihoon9835:wlgns9835@cluster0.xh3ds.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        client = MongoClient(uri)

        database = client["jihoon9835"]
        collection = database["user_data"]
        result = list(collection.find({}))
        result = convert_objectid(result)
        client.close()

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)
    return {"data": result}

@app.get("/user_data/{data_id}")
def read_user_data(data_id: str):
    try:
        uri = "mongodb+srv://jihoon9835:wlgns9835@cluster0.xh3ds.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        client = MongoClient(uri)

        database = client["jihoon9835"]
        collection = database["user_data"]
        try:
            data_id = ObjectId(data_id)
        except:
            print("Invalid ObjectId")
        result = collection.find_one({"_id":data_id})
        result = convert_objectid(result)
        client.close()

    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)
    return {"data": result}

@app.post("/user_data/")
def create_user_data(data):
    try:
        uri = "mongodb+srv://jihoon9835:wlgns9835@cluster0.xh3ds.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        client = MongoClient(uri)
        database = client["jihoon9835"]
        collection = database["user_data"]
        data = {
            "user_id":data.user_id,
            "title":data.title,
            "painter":data.painter,
            "fact":data.fact,
            "response":data.response,
            "image_id":data.data_id,
            "image":data.image
        }
        result = collection.insert_one(data)
        client.close()
    except Exception as e:
        raise Exception(
            "The following error occurred: ", e)
    return {"id": str(result.inserted_id), "data": data}





