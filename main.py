from fastapi import FastAPI

app = FastAPI()

@app.get("/helloworld")
async def root():
    return {"message": "Hello World"}

# 127.0.0.1:8000/teste1
@app.get("/funcaoteste")
async def funcaoteste():
    return{"teste": "deu certo"}