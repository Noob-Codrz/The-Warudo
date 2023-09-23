from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from schemas.schemas import UserPasswd
from sqlalchemy.orm import Session
from fastapi import Depends
from database.database import get_db

SECRET_KEY = "0c8ee754e6da597eb54c40e33666422f8b6b6edf11960208f626fb0df738d1cb"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


passwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")




def verify(passwd, hashed_passwd):
    return passwd_context.verify(passwd, hashed_passwd)


def hash_passwd(passwd):
    return passwd_context.hash(passwd)

