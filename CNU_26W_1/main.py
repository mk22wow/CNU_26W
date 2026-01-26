from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# from app.week2.practice1 import router as practice1_router
# from app.week2.practice2 import router as practice2_router
# from app.week2.practice3 import router as practice3_router

app = FastAPI()

# app.include_router(practice1_router)
# app.include_router(practice2_router)
# app.include_router(practice3_router)

items: list[dict] = [{'id':1, 'data':'apple', 'price': '1$'}, {'id':2, 'data':'banana', 'price': '2$'}, {'id':3, 'data':'cherry', 'price': '3$'}]

# items에 price 정보 추가

class ItemCreate(BaseModel):
    data: str
    price: str

@app.post('/items') # data, price 값 입력 받기
def create_item(payload: ItemCreate):
    item: dict = {'id': len(items)+1, **payload.model_dump()}
    items.append(item)
    return item

@app.get('/items') # 실습 3
def get_items():
    return {"data": items}

@app.get('/items/{item_id}') # 실습 3
def get_item_by_id(item_id: int):
    for item in items:
        if item.get('id') == item_id:
            return item
    raise HTTPException(status_code=404, detail='Item not found')

@app.get(path="/")
async def root():
    return {"message": "Hello World"}

@app.get('/search/items') # data(쿼리 파라미터)를 이용한 price 검색
def search_price(name: str):
    for item in items:
        if(item['data'] == name):
            return {"price": item['price']}
    raise HTTPException(status_code=404, detail='Item not found')

# @app.get(path="/items")
# async def get_items():
#     return {"items": items}

# @app.get(path='/items/{id}')
# async def get_item_by_id(id:int):
#     if id<0 or id>=len(items):
#         return {"error": "Invalid ID"}
#     return {"items": items[id]}

@app.get(path='/items/')
async def search_item(q: str):
    for item in items:
        if(item == q):
            return {"result": "OK"}
    return {"result": "Not OK"}
