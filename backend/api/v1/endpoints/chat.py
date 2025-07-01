
from fastapi import APIRouter
from services.chat_service import ChatService

router  = APIRouter()
chatService = ChatService()

@router.get("/chat")
async def chat():
    return {"response": await chatService.generar_chat()}

