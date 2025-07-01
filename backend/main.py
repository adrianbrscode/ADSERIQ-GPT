from fastapi import FastAPI

#from api.v1.endpoints.chat import chat
#from services.chat_service import ChatService
from fastapi import FastAPI
from api.v1.endpoints import chat

app = FastAPI(title="ADSER-IQ")

app.include_router(chat.router)

"""
app = FastAPI()

@app.get("/")
def hola():
    return {"msg:" : "hola mundo"}
"""

#prueba = ChatService()
#prueba.generar_chat()

