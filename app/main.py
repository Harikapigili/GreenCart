from fastapi import FastAPI
from app.routers import routers as products
from app.database import engine,Base
from app.config import get_settings
settings=get_settings()
app=FastAPI(
    title="GreenCart",
    description="A quality Product Store",
    version="1.0.0",
    debug=settings.DEBUG
)
Base.metadata.create_all(bind=engine)
app.include_router(products.router)
@app.get("/")
def root():
    return{"message":"Welcome to GreenCart","status":"running"}
@app.get("/health")
def health_check():
    return {"status":"healthy"}