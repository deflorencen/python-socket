import socket
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

                if(option == "1"):
                    command.create_user(server)

                if not option:
                    print('Server is stoped') # My propose to add here print() with information, that server is stoped 
                    break
