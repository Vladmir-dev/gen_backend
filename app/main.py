from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.query import router as query_router

app = FastAPI(
    title="Travel Advisor AI API",
    description="API for travel-related queries using DeepSeek LLM",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(query_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to Travel Advisor AI API"}
