from fastapi import FastAPI
from models import Problem, engine

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
