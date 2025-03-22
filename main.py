from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

# 127.0.0.1:8000/teste1
@app.get("/teste")
async def funcaoteste():
    return{"teste": True, "número aleatório": random.randint(0, 20000)}