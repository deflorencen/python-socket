import json
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


# SENDING A MESSAGE TO THE CLIENT FROM SERVER
def send_request_to_client(server, message_to_client):
    server.sendall(f"{message_to_client}".encode('utf-8'))

# SENDING A MESSAGE TO THE SERVER FROM CLIENT
def send_request_to_server(client, message_to_server) -> str:
    client.sendall(f"{message_to_server}".encode('utf-8'))


# ACCEPTANCE OF MESSAGES BY THE CLIENT FROM THE SERVER
def get_message_from_server(client) -> str:
    server_message = client.recv(1024).decode('utf-8')
    return server_message


def get_message_from_client(server) -> str:
    client_message = server.recv(1024).decode('utf-8')
    return client_message

# ACCEPTANCE OF DATA BY SERVER FROM THE CLIENT
def get_from_client(server) -> dict:
    user_request = server.recv(1024).decode('utf-8')
    user_info_json = json.loads(user_request)

    return user_info_json


def hash_password(password) -> str:
    ph = PasswordHasher()
    hash_password = ph.hash(password)
    return hash_password

def check_password(password):
    ph = PasswordHasher()
    check = ph.verify(password, input())
    pass


def create_user(server):
    send_request_to_client(server, "\n\tCREATING USER:\n")

    user_info_json = get_from_client(server)
    print("USER DATA:", user_info_json)

    fname = user_info_json["First name"]
    lname = user_info_json["Last name"]
    with open(f'users/{fname}_{lname}.json', 'w') as data_file_json:
        json.dump(user_info_json, data_file_json)

    message_to_client = "\n\tUser successfully created."
    send_request_to_client(server, message_to_client)

def check_account_status(server):
    send_request_to_client(server, "\n\tInformation about account:\n")

    user_info_json = get_from_client(server)
    print("USER DATA:", user_info_json)

    fname = user_info_json["First name"]
    lname = user_info_json["Last name"]
    with open(f'users/{fname}_{lname}.json', 'r') as show_data_file:
        data = json.load(show_data_file)

    message_to_client = f'\n\tUzytkownik: {data["First name"]} {data["Last name"]}. \n' \
                        f"\tNumer konta: {data['KEY']}. \n" \
                        f"\tSaldo: {data['Balance']:.2f} PLN \n"
    send_request_to_client(server, message_to_client)

def payment_on_account(server):
    send_request_to_client(server, "\n\tPayment:\n")

    user_info_json = get_from_client(server)
    print("USER DATA:", user_info_json)

    fname = user_info_json["First name"]
    lname = user_info_json["Last name"]
    balance = user_info_json["Balance"]
    password = user_info_json["Password"]

    if float(balance) <= 0:
        send_request_to_client(server, "The amount cannot be negative or zero! ")
    else:
        with open(f'Users/{fname}_{lname}.json', 'r') as file_to_changing:
            data = json.load(file_to_changing)
            ph = PasswordHasher()

            if (ph.verify(data["Password"], password)):
                data["Balance"] += float(balance)
                with open(f'Users/{fname}_{lname}.json', 'w') as file_to_changing:
                    json.dump(data, file_to_changing)

    message_to_client = f"Kwota po operacji wynosi: {data['Balance']:.2f} PLN"
    send_request_to_client(server, message_to_client)
