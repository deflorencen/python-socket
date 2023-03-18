# SENDING A MESSAGE TO THE CLIENT
def send_to_client(server, message_to_client):
    server.sendall(f"{message_to_client}".encode('utf-8'))

# ACCEPTANCE OF MESSAGES BY THE CLIENT FROM THE SERVER
def get_message_from_server(client):
    server_message = client.recv(1024).decode('utf-8')
    return server_message

