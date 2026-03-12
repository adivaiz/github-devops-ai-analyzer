from fastapi import FastAPI
from backend.github_listener import router

app = FastAPI()

# חיבור ה-router של GitHub לשרת
app.include_router(router)

@app.get("/")
def home():
    return {"message": "DevOps AI Analyzer running"}
