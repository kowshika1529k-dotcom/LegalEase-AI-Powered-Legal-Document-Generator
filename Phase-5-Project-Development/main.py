from fastapi import FastAPI
from routes import router

app = FastAPI(title="LegalEase",
              description="AI-Powered Legal Document Generator")

app.include_router(router)

@app.get("/")
def home():
    return {"message": "Welcome to LegalEase"}
