from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI()

@app.get("/")
def home_root():
    return {
        "Hello, This is Home page"
        }

# Pydantic models (schemas)
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=6)

class User(BaseModel):
    username: str

class Token: 
    access_Token: str
    token_type: str