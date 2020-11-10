# Online chat room
An online room, post messages to the room, and have others in the same room see those messages immediately

# Overview
Chat room is built based on https://channels.readthedocs.io/en/stable/tutorial/part_1.html
A simple chat server that will have:
- An index view that lets you type the name of a chat room to join.
- A room view that lets you see messages posted in a particular chat room.

The room view will use a WebSocket to communicate with the Django server and listen for any messages that are posted.

### room.html
In a given chat room, a new WebSocket object is created via JS. It has the host and the room name in its URL.

When Submit button is clicked, the value of the chat message input field is read and sent to 
the WebSocket. Afterwards, the value of this field is cleared.

In the log field, whenever a new message appears in the WebSocket, it's attached to that field.

### WebSocket 
A basic consumer accepts WebSocket connections on the path /ws/chat/ROOM_NAME/ that takes any message it receives on 
the WebSocket and echos it back to the same WebSocket.
