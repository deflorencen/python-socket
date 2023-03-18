import socket
import command

# SERVER VARIABLE
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# WE SHOW WHAT IP ADDRESS AND PORT WE WORK ON
server.bind(('127.0.0.1', 12345))

# HOW MUCH A CONNECTED PERSON CAN ACCEPT OUR SERVER AT A TIME
server.listen(0)

# TO ACCEPT CONNECTED FROM THE CLIENT
server, addr = server.accept()
print(f"CONNECTED:\n{server}\n{addr}")

command.send_to_client(server, "Hello, client!")

# RECEIVING MESSAGES FROM THE CLIENT TO THE SERVER
client_request = server.recv(1024)
message = client_request.decode('utf-8')
print(f"USER MESSAGE:\n\t{message}")
