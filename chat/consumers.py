import json

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add(
            'chatRoom',
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            "chatRoom",
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        key = text_data_json["key"]
        iv = text_data_json["iv"]
        username = text_data_json["username"]
        await self.channel_layer.group_send(
            "chatRoom", {
                "type": "sendMessage",
                "message": message,
                "key":key,
                "iv": iv,
                "username": username,
            })

    async def sendMessage(self, event):

        message = event["message"]
        username = event["username"]
        key = event["key"]
        iv = event["iv"]
        await self.send(text_data=json.dumps({"message": message, "username": username, "key":key , "iv":iv}))
