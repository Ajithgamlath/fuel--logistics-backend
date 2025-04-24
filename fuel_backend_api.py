from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Fuel Logistics API is live!"}