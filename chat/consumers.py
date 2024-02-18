import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.save_message(message)

        await self.send(text_data=json.dumps({
            'message': message
        }))

    @sync_to_async
    def save_message(self, message):
        Message.objects.create(user=self.scope['user'], content=message)
