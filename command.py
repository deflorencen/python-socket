import json
from argon2 import PasswordHasher

# SENDING A MESSAGE TO THE CLIENT FROM SERVER
def send_request_to_client(server, message_to_client):
    server.sendall(f"{message_to_client}".encode('utf-8'))

# ACCEPTANCE OF MESSAGES BY THE CLIENT FROM THE SERVER
def get_message_from_server(client):
    server_message = client.recv(1024).decode('utf-8')
    return server_message

# SENDING A MESSAGE TO THE SERVER FROM CLIENT
def send_request_to_server(client, message_to_server):
    client.sendall(f"{message_to_server}".encode('utf-8'))

def get_from_client(server):
    user_request = server.recv(1024).decode('utf-8')
    user_info_json = json.loads(user_request)

    return user_info_json

def hash_password(password):
    hash_password = PasswordHasher.hash(password)
    return hash_password

def create_user(server):
    send_request_to_client(server, "\n\tCREATING USER:")

    user_info_json = get_from_client(server)
    print("USER DATA:", user_info_json)

    fname = user_info_json["First name"]
    lname = user_info_json["Last name"]
    with open(f'users/{fname}_{lname}.json', 'w') as data_file_json:
        json.dump(user_info_json, data_file_json)