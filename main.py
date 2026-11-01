

from fastapi import FastAPI

app = FastAPI(
    title="Cloud Deployment Tool",
    description="A Python application for automated cloud deployment and health monitoring",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Cloud Deployment Tool!",
        "status": "Application is running"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "Cloud Deployment Tool"
    }
