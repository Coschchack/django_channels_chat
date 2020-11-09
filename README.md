# Online chat room
An online room, post messages to the room, and have others in the same room see those messages immediately

# Overview
Chat room is built based on https://channels.readthedocs.io/en/stable/tutorial/part_1.html
A simple chat server that will have:
- An index view that lets you type the name of a chat room to join.
- A room view that lets you see messages posted in a particular chat room.

The room view will use a WebSocket to communicate with the Django server and listen for any messages that are posted.

