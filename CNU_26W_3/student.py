from typing import Optional
from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException

class_router = APIRouter(prefix="/myclass", tags=["class"])

class Myclass(BaseModel):
    class_id: int
    class_name: str
    class_time: int

Class1 = [
    Myclass(class_id=1, class_name='CS', class_time=2),
    Myclass(class_id=2, class_name='Math', class_time=3),
    Myclass(class_id=3, class_name='English', class_time=3)
]

current_id = 3

@class_router.get(
    '',
    status_code=200,
    summary="클래스 항목 조회"
)
def get_class():
    return Class1


@class_router.get(
    '/{id}',
    status_code=200,
    response_model=Myclass,
    summary="원하는 클래스 조회"
)
def get_class_by_id(id: int):
    for temp in Class1:
        if(temp.class_id == id):
            return temp
    raise HTTPException(status_code=404, detail='Class not found')

class NewClass(BaseModel):
    class_name: str = Field(examples=["CS"])
    class_time: int = Field(ge=1, examples=[3])

@class_router.post(
    '',
    status_code=201,
    summary="클래스 추가"
)
def add_class(payload: NewClass):
    global current_id
    current_id+=1
    new_c = Myclass(class_id=current_id, **payload.model_dump())
    Class1.append(new_c)
    return Class1

class ClassUpdate(BaseModel):
    class_name: str
    class_time: int = Field(ge=1)

@class_router.put(
    '/update/{id}',
    status_code=200,
    responses={404: {"description":"Class not found"}},
    summary="클래스 전체 수정",
    # deprecated=True
)
def update_class(id:int, payload: ClassUpdate):
    for i, temp in enumerate(Class1):
        if(temp.class_id == id):
            new_class = Myclass(class_id=id, **payload.model_dump())
            Class1[i] = new_class
            return new_class
    raise HTTPException(status_code=404, detail="Class not found")

class ClassPatch(BaseModel):
    class_name: Optional[str] = None
    class_time: Optional[int] = Field(None, ge=1)


@class_router.patch(
    '/patch/{id}',
    status_code=200,
    responses={404: {"description": "Class not found"}},
    summary="클래스 부분 수정",
    response_description="수정된 클래스의 전체 정보"
)
def patch_class(id: int, payload: ClassPatch):
    for temp in Class1:
        if temp.class_id == id:
            if payload.class_name is not None:
                temp.class_name = payload.class_name
            if payload.class_time is not None:
                temp.class_time = payload.class_time
            return temp
    raise HTTPException(status_code=404, detail='Class not found')


@class_router.delete(
    '/delete/{id}',
    status_code=204,
    responses={404: {"description": "Class not found"}},
    summary="클래스 삭제"
)
def delete_item(id: int):
    for temp in Class1:
        if temp.class_id == id:
            Class1.remove(temp)
            return
    raise HTTPException(status_code=404, detail='Class not found')
