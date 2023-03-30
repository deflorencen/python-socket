import socket
import json
import command
import random
from argon2 import PasswordHasher

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect(("127.0.0.1", 12345))

        while True:
            option = input("\n\t#######################################"
                           "\n\t1: Create user"
                           "\n\t2: Check account status"
                           "\n\t3: Payment on account"
                           "\n\t4: Make the payment"
                           "\n\t5: Transfer money to another account"
                           "\n\t#######################################"
                           "\n"
                           "\nCHOOSE YOU OPTION: ")

            if (option == "1"):
                command.send_request_to_server(client, "1")

                print(command.get_message_from_server(client))

                fname = input("First name: ")
                lname = input("Last name: ")
                pesel = input("PESEL: ")
                password = input("Password: ")
                hash_password = command.hash_password(password)
                id = 0

                user = {"First name": fname, "Last name": lname, "KEY": id, "PESEL": pesel, "Password": hash_password,
                        "Balance": 0}
                send_data = json.dumps(user)
                command.send_request_to_server(client, send_data)

                server_message = command.get_message_from_server(client)
                print(server_message)

            elif (option == "2"):
                command.send_request_to_server(client, "2")

                print(command.get_message_from_server(client))

                fname = input("First name: ")
                lname = input("Last name: ")

                user = {"First name": fname, "Last name": lname}
                data_to_find = json.dumps(user)
                command.send_request_to_server(client, data_to_find)

                server_message = command.get_message_from_server(client)
                print(server_message)

            elif (option == "3"):
                command.send_request_to_server(client, "3")

                print(command.get_message_from_server(client))

                fname = input("First name:")
                lname = input("Last name:")
                balance = input("Sum to payment:")
                password = input("Password:")
                user = {"First name": fname, "Last name": lname, "Balance": balance, "Password": password}

                data_to_changing = json.dumps(user)
                command.send_request_to_server(client, data_to_changing)

                server_message = command.get_message_from_server(client)
                print(server_message)

            elif (option == "4"):
                command.send_request_to_server(client, "4")

                print(command.get_message_from_server(client))

                fname = input("First name:")
                lname = input("Last name:")
                balance = input("Sum to payment:")
                password = input("Password:")
                user = {"First name": fname, "Last name": lname, "Balance": balance, "Password": password}

                data_to_changing = json.dumps(user)
                command.send_request_to_server(client, data_to_changing)

                server_message = command.get_message_from_server(client)
                print(server_message)

            elif (option == "5"):
                command.send_request_to_server(client, "5")

                print(command.get_message_from_server(client))

                owner_fname = input("First name:")
                owner_lname = input("Last name:")
                money_to_transfer = input("Money to transfer: ")
                password = input("Password:")
                print("Transfer to..")
                fname_t = input("First name:")
                lname_t = input("Last name:")
                users = {"First name": owner_fname, "Last name": owner_lname, "Password": password, "Money to transfe": money_to_transfer,}

                data_to_changing = json.dumps(users)
                command.send_request_to_server(client, data_to_changing)




            elif(option == "q"):
                command.send_request_to_server(client, "q")
                break



except ConnectionRefusedError:
    print("NOT CONNECTION..")