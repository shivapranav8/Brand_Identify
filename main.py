# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello(name: str = "Shiva"):
    return {"message": f"hi {name}"}
