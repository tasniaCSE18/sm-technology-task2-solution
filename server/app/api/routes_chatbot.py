from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatRequest, ChatResponse
from app.services.chatbot_service import chatbot_service
from app.services.product_service import product_service

router = APIRouter(prefix="/api", tags=["Chatbot"])

@router.get("/products")
async def get_products():
    
    try:
        products = await product_service.fetch_all_products()
        return {
            "total": len(products),
            "products": products
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Chat with the AI assistant about products
    
    Example queries:
    - "Tell me about Kiwi"
    - "What is the price of mango?"
    - "Show me products with ratings above 4"
    - "Do you have any electronics?"
    """
    try:
        if not request.message.strip():
            raise HTTPException(status_code=400, detail="Message cannot be empty")
        
        response = await chatbot_service.process_message(request.message)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))