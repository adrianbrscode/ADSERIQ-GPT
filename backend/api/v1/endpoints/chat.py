from fastapi.responses import StreamingResponse
from fastapi import APIRouter
from services.chat_service import ChatService

router  = APIRouter()
chatService = ChatService()

#@router.get("/chat")
#async def chat():
#    return {"response": await chatService.generar_chat()}

@router.get("/chat-stream", response_class=StreamingResponse)
async def chat_stream():
    return StreamingResponse(chatService.generar_chat(), media_type="application/x-ndjson")
