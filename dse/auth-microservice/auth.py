from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError
from models import UserInDB

SECRET_KEY = "clave-super-secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Base de datos simulada con contraseña en texto plano
fake_users_db = {
    "anthony": {
        "username": "anthony",
        "full_name": "Anthony Nichols",
        "hashed_password": "12345678",  # Ahora no es hash, es texto plano
    }
}

def get_user(username: str) -> Optional[UserInDB]:
    user_dict = fake_users_db.get(username)
    if user_dict:
        return UserInDB(**user_dict)
    return None

def verify_password(plain_password, stored_password):
    # Comparación directa sin hash
    return plain_password == stored_password

def authenticate_user(username: str, password: str) -> Optional[UserInDB]:
    user = get_user(username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str) -> Optional[str]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None
