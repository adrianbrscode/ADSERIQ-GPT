from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hola():
    return {"msg:" : "hola mundo"}