import json

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
                {"role": "user", "content": "hola, eres humana"}
            ],
            stream=True
        )
        print("hola")
        for chunk in completion:
            delta = chunk.choices[0].delta
            finish_reason = chunk.choices[0].finish_reason

            if delta.content:
                yield json.dumps({"content":delta.content})+"\n"
                print(delta.content)

            if finish_reason is not None:
                print("termino")
                yield json.dumps({"finish_reason":finish_reason})+"\n"
                break
        #return completion.choices[0].message.content