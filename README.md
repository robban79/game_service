# game_service

A simple REST API server made with flask

## Usage
Run 10.0.2.2: port, 5000 to get hold of localhost on your device

### Add user
POST: /user/{name: "Your game name"}
#### response:
201 - {id, "Your game id"}
422 - User already exsist

#### Note; hold on to your game id, you will need it

### Get users
get  /user/{id, "Your game id"}
#### response:
200 - {users:, [name: "user-1",..., name: "user-n" ]}
403 - Forbidden/// Not a vald game id

### Add message
POST: /message/{id, "Your game id", message: "Your message"}
#### response:
201 - {id, "Your game id"}
403 - Forbidden/// Not a vald game id

### Get messages
get  /user/{id, "Your game id"}
#### response:
200 - {Messages:, [{message_id: id, name: "user-xx", message: "the messag"}..., {message_id: id, name: "user-xx", message: "the messag"} ]}
403 - Forbidden/// Not a vald game id
