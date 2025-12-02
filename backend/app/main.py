from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "skibidi"}

@app.get("/test")
def test():
    return {"message": "67"}
