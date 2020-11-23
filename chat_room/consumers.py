import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'
        self.user_name = self.scope['session']['user_name']
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        # if we do not call accept() then the connection will be rejected and closed
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(self, text_data):
        """
        Receive message from a Websocket, and send it to the room group.
        """
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat.message",
                "user_name": self.user_name,
                "message": message,
            }
        )

    async def chat_message(self, event):
        """
        When a message hits the room group, send it to the WebSocket.
        """
        await self.send(text_data=json.dumps({
            'user_name': event['user_name'],
            'message': event['message'],
        }))
