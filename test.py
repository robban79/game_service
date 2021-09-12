#!/usr/bin/env python3
import uuid

import requests

# BASE = "http://192.168.50.85:5000/"

BASE = "http://127.0.0.1:5000/"

# Ge users
response = requests.get(BASE + "user/")
print(response.json())


# Add two users
response = requests.post(BASE + "user/", {"name": "user1"})
print(response.json())
id_user_1 = "1"
if f'{response.json()}'.find("id") >= 0:
    id_user_1 = response.json()["id"]

response = requests.post(BASE + "user/", {"name": "user2"})
print(response.json())
id_user_2 = ""
if f'{response.json()}'.find("id") >= 0:
    id_user_2 = response.json()["id"]

# Get users again
response = requests.get(BASE + "user/", {"id": id_user_1})
print(response.json())

response = requests.put(BASE + "user/")
print(response.json())

#################
#Add messages
##################
print("Set message")

for i in range(0, 11, 1):
    response = requests.post(BASE + "message/", {"id": id_user_1,
                                                 "message": "hello you mother fucker "+f'{i}' })
    print(response.json())
    response = requests.post(BASE + "message/", {"id": id_user_2,
                                                 "message": "hello back you mother fucker " + f'{i}'})
    print(response.json())

print("Get all messages")
response = requests.get(BASE + "message/", {"id": id_user_1})
print(response.json())

#################
#Send crapy message
##################

print("Test add message crap user")
response = requests.post(BASE + "message/", {"id": f'{uuid.uuid4()}'.replace("-", ""), "message": "will not work" })
print(response.json())

print("Test get message crap user")
response = requests.get(BASE + "message/", {"id": f'{uuid.uuid4()}'.replace("-", "")})
print(response.json())

