from pydantic import BaseModel, HttpUrl,EmailStr,validator
from uuid import UUID
from typing import Optional
from datetime import datetime
#from fastapi import Form,UploadFile,File


class BaseEvent(BaseModel):
    title: str
    description: Optional[str]
    poster:UUID
    location : Optional[str]
    location_link:Optional[HttpUrl]
    registration_link:Optional[HttpUrl]
    timings:Optional[datetime]
    publish:bool

    class Config:
        orm_mode = True


#class RequestEvent(BaseModel):
    #title: str=Form(...)
    #description: Optional[str]=Form(None)
    #poster:UploadFile=File()
    #poster: UUID=Form(...)
    #location : Optional[HttpUrl]=Form(None)
    #registration_link:Optional[HttpUrl]=Form(None)
    #timings:Optional[datetime]=Form(None)
    #publish:bool=Form(...)

class RequestEvent(BaseEvent):
    pass


class ResponseEvent(BaseEvent):
    id:int
    
class CreateUser(BaseModel):
    name:str
    email:EmailStr
    password:str

class ResponseUser(BaseModel):
    id:int
    name:str
    email:str
    is_admin:bool

    class Config:
        orm_mode = True

class EventCardResponse(BaseModel):
    id:int
    title: str
    poster:str
    timings:Optional[datetime]

    class Config:
        orm_mode = True



class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id : Optional[str]=None


class LoginResponse(ResponseUser,Token):
    pass

    