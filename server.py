from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models.connection import get_db
from models.models import User
from models import schema 

app = FastAPI()

@app.post("/user/register", response_model=schema.RegisterResponse)
async def create_user(user: schema.UserRegister, db: Session = Depends(get_db)):
    new_user = User(user_id = user.user_id, user_pw = user.user_pw,
                    name = user.name, email = user.email, role = user.role )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {
        "message" : "회원가입을 축하드립니다."
    }

@app.post("/user/login", response_model=schema.LoginResponse)
async def login_user(user: schema.UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.user_id == user.user_id).first() 
    if not db_user:
        raise HTTPException(
            status_code=404,
            detail="존재하지 않는 사용자입니다."
        )

    if db_user.user_pw != user.user_pw:
        raise HTTPException(
            status_code=404,
            detail="비밀번호가 일치하지 않습니다."
        )
    return {
        "message": "로그인 성공"
    }
     