from pydantic import BaseModel
from fastapi import Header
from typing import Optional
from datetime import datetime

# request
class UserRegister(BaseModel):
    user_id: str
    user_pw: str
    name: str
    email: str
    phone: str
    role: int

class UserLogin(BaseModel):
    user_id: str
    user_pw: str

# firebase 로그인
class SocialUserLogin(BaseModel):
    Authorization: str

class RegisterResponse(BaseModel):
    message: str

    class Config:
        orm_mode = True

class LoginResponse(BaseModel):
    message: str

    class Config:
        orm_mode = True    

#차량 등록
class registerVehicle(BaseModel):
    vehicle_num: str
    is_disabled: bool
    registered_by: int

class requestDisabled(BaseModel):
    registered_by: int

#차량 조회
class getVehicle(BaseModel):
    vehicle_num: str
    is_disabled: bool
    registered_by: Optional[int] = None
    approved_by: Optional[int] = None
    approved_at: Optional[datetime] = None

    class Config:
        orm_mode = True
