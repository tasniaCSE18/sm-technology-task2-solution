from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes_chatbot import router

app = FastAPI(
    title="E-Commerce Chatbot API",
    description="AI-powered chatbot for product queries using Groq LLM",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to E-Commerce Chatbot API",
        "docs": "/docs",
        "endpoints": {
            "products": "/api/products",
            "chat": "/api/chat"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)