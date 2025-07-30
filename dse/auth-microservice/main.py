from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth import authenticate_user, create_access_token, decode_token, get_user
from models import User
from datetime import timedelta

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=30)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    username = decode_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = get_user(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return User(username=user.username, full_name=user.full_name)

