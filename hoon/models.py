from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, TIMESTAMP, DateTime
from sqlalchemy.sql import func
from app.db.database import engine
from datetime import datetime
from sqlalchemy import Boolean
#import pytz

Base = declarative_base()

# def get_kst():
#     return datetime.now(pytz.timezone("Asia/Seoul"))

# user 테이블
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(255), primary_key=True)
    user_pw = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    name = Column(String(255),nullable=False)
    phone = Column(String(13), unique=True, nullable=False)
    role = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# vehicle 테이블
class Vehicle(Base):
    __tablename__ = 'vehicles'

    vehicle_num = Column(String(8), primary_key=True)
    is_disabled = Column(Boolean, default=False, nullable=False)
    registered_by = Column(Integer, autoincrement=True)
    approved_by = Column(Integer, autoincrement=True)
    approved_at = Column(DateTime(timezone=True))
