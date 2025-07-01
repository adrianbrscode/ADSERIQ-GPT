from openai.resources.containers.files import content
from openai.types import completion

#from clients.openai_client import client
from clients.openai_client import client


class ChatService:



    async def generar_chat(self):
        completion = client.chat.completions.create(
            model="gpt-4.1-nano",
            messages=[
                {"role": "developer",
                 "content": "Te llamas Nina, y eres una asistente de la empresa AdserIQ, presentate como tal"},
                {"role": "user", "content": "hello"}
            ],
            stream=False
        )

        #for chunk in completion:
        #    print(chunk.choices[0].delta)

        return completion.choices[0].message.content