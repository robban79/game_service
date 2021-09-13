# game_service

A simple REST API server made with flask

## Dependencies
Flask, Flask-RESTful, pyOpenSSL

## Usage
Run chat_server.py, Note/Warning: Default starts in debug mode, no ssl and broadcast.
Setup client to 10.0.2.2: port, 5000 to get hold of localhost on your device

### Add user
POST: /user/{name: "Your game name"}
#### response:
201 - {id, "Your game id"}
422 - User already exsist

#### Note; hold on to your game id, you will need it

### Get users
get  /user/{id, "Your game id"}
#### response:
200 - {[{id: null,name: "user-1"},..., {id: null, name: "user-n"0 ]}
403 - Forbidden/// Not a vald game id

### Add message
POST: /message/{id, "Your game id", message: "Your message"}
#### response:
201 - {id, "Your game id", message_id= 1, message: "your message"}
403 - Forbidden/// Not a vald game id

### Get messages
get  /user/{id, "Your game id"}
#### response:
200 - {Messages:, [{message_id: id, name: "user-xx", message: "the messag"}..., {message_id: id, name: "user-xx", message: "the messag"} ]}
403 - Forbidden/// Not a vald game id
