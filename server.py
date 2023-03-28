import socket

from argon2.exceptions import InvalidHash

import command

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind(("127.0.0.1", 12345))
    server.listen(0)

    print("\n\tSERVER IS WORKING...")

    while True:
        server, address = server.accept()

        with server:

            while True:
                option = server.recv(1024).decode("utf-8")

                if (option == "1"):
                    command.create_user(server)

                elif (option == "2"):
                    command.check_account_status(server)

                elif (option == "3"):
                        command.payment_on_account(server)

                if (option == "q"):
                    print('Server is stoped')
                    break