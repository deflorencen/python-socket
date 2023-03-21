import socket
import json
import command
import random

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

                fname = input("Fisrt name: ")
                lname = input("Last name: ")
                pesel = input("PESEL: ")
                password = input("Password: ")
                hash_password = command.hash_password(password)
                id = 0

                user = {"First name": fname, "Last name": lname, "KEY:": id, "PESEL": pesel, "Password:": hash_password,
                        "Balance": 0}
                send_data = json.dumps(user)
                command.send_request_to_server(client, send_data)



            elif(option == "q"):
                command.send_request_to_server(client, "q")
                break




except ConnectionRefusedError:
    print("NOT CONNECTION..")