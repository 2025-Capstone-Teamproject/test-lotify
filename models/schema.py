from pydantic import BaseModel
# request 객체
class UserRegister(BaseModel):
    user_id: str
    user_pw: str
    name: str
    email: str
    role: int

class UserLogin(BaseModel):
    user_id: str
    user_pw: str

# response 객체
class RegisterResponse(BaseModel):
    message: str

    class Config:
        orm_mode = True

class LoginResponse(BaseModel):
    message: str

    class Config:
        orm_mode = True        