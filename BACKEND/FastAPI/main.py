from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "¡Hola FastAPI!"}

@app.get("/2")
async def root2():
    return {"message": "¡Cuánto tiempo!"}