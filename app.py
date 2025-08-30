from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "here we go buddy sky is the limit!!"}

@app.get("/user/{name}")
def get_user(name: str, age: int):
    return {"user": name, "age": age}

