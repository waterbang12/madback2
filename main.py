from fastapi import FastAPI
from pydantic import BaseModel

# FastAPI 애플리케이션 인스턴스 생성
app = FastAPI()

# 데이터 모델 정의
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = 0.0

# 기본 루트
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# GET 요청 처리
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}

# POST 요청 처리
@app.post("/items/")
def create_item(item: Item):
    total_price = item.price + (item.price * item.tax)
    return {
        "name": item.name,
        "description": item.description,
        "price": item.price,
        "tax": item.tax,
        "total_price": total_price
    }

