import datetime
import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.user_name = None
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.group_send("I'm leaving the chat. Bye!")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        self.user_name = text_data_json.get("user_name", self.user_name)
        await self.group_send(text_data_json['message'])

    async def group_send(self, message):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "user_name": self.user_name,
                "message": message,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'user_name': event['user_name'],
            'message': event['message'],
            'timestamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }))
