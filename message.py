from flask_restful import Resource, reqparse
from the_chat import TheChat


class ChatMessage:
    count = 0

    def __init__(self, user_id, message):
        self.user_id = user_id
        self.message = message
        ChatMessage.count += 1
        self.message_id = ChatMessage.count

    def to_string(self):
        return f'message: {self.message}'


class MessageApi(Resource):

    def __init__(self):
        self.message_add_args_parser = reqparse.RequestParser()
        self.message_add_args_parser.add_argument("id", type=str,
                                           help="The id of the user")
        self.message_add_args_parser.add_argument("message", type=str,
                                           help="The chat message")

        self.message_read_args_parser = reqparse.RequestParser()
        self.message_read_args_parser.add_argument("id", type=str,
                                                  help="Need valid user id")


    @staticmethod
    def abort_if_user_not_exist(user_id):
        for user in TheChat.users:
            if user.user_id == user_id:
                return True
        return False

    def post(self):
        """
        post
        /message/ {id: id, message: "User message"}
        return: id
        """
        print("POST: Write message")
        args = self.message_add_args_parser.parse_args()
        user_id = args["id"]
        print(user_id)
        if not MessageApi.abort_if_user_not_exist(user_id):
            return "Forbidden///", 403
        message = ChatMessage(user_id, args["message"])
        TheChat.messages.append(message)
        return {"id": user_id}, 201

    @staticmethod
    def get_user_from_id(user_id):
        for user in TheChat.users:
            if user.user_id == user_id:
                return user.name
        return ""

    def get(self):
        """
        get
        /user
        return: id
        """
        print("GET: Get messages")
        args = self.message_read_args_parser.parse_args()
        user_id = args["id"]
        name = MessageApi.get_user_from_id(user_id)
        if name == "":
            return "Forbidden///", 403

        messages = []
        for message in TheChat.messages:
            messages.append({"message_id": message.message_id, "name":  MessageApi.get_user_from_id(message.user_id), "message": message.message})
        answer = {"Messages:": messages}
        print(answer)
        return answer, 200

    def put(self):
        print("PUT: Testprint out messates")
        for message in TheChat.messages:
            print(message.to_string())

        return "", 200
