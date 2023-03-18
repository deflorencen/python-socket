import socket
import command

# CLIENT VARIABLE
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# CONNECTION OF THE CLIENT TO THE SERVER
client.connect(("127.0.0.1", 12345))

server_message = command.get_message_from_server(client)
print(server_message)

# SENDING DATA TO THE SERVER FROM THE CLIENT
message_to_server = "Wpisz wiadomosc dla servera:"
client.sendall(message_to_server.encode('utf-8'))
