from socket import *

server = socket(AF_INET, SOCK_STREAM)

server.bind(
    ("127.0.0.1", 7000)
)

server.listen(2)
print("Server is running...")

user, addr = server.accept()
print(f"CONNECTED:\n\t{user}\n\t{addr}\n")

user.send("You are connected!".encode("utf-8"))

msg = user.recv(1024).decode("utf-8")
print(f"USER MSG:\n\t{msg}\n")

# while True: