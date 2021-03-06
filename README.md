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
https://channels.readthedocs.io/en/stable/topics/channel_layers.html
Each application instance (each open WebSocket) results in a single Consumer instance, and as we have channel layers enabled, Consumers will generate a unique channel name for themselves, and start listening on it for events.

This means we can send those consumers events from outside the process (from other consumers) and they will react to them and run code just like they would events from their client connection.

When a user posts a message, a JavaScript function will transmit the message over WebSocket to a ChatConsumer. 
The ChatConsumer will receive that message and forward it to the group corresponding to the room name. 
Every ChatConsumer in the same group (and thus in the same room) will then receive the message from the group and 
forward it over WebSocket back to JavaScript, where it will be appended to the chat log.

The information (messages) between the client and server are sent via JSONs. Thanks to that, so more information can 
be added at any time simply by extending the JSON fields.

## Running the chat in Dockers
1. From the root folder of the repository, build the needed image(s):
`docker-compose -f docker/docker-compose.yml build`
2. Start the chat:
`docker-compose -f docker/docker-compose.yml up`
3. Access the chat in the browser by:
`http://127.0.0.1:8000/chat`
4. At the end, put the containers down:
`docker-compose -f docker/docker-compose.yml down`
