from pydantic import BaseModel

# Modelo de usuario que se devuelve al frontend
class User(BaseModel):
    username: str
    full_name: str | None = None

# Modelo interno para manejo de autenticación
class UserInDB(User):
    hashed_password: str
