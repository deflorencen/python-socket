from socket import *

client = socket(AF_INET, SOCK_STREAM)

client.connect(("127.0.0.1", 7000))

data = client.recv(1024)
msg = data.decode("utf-8")

print(f"SERVER MSG:\n\t{msg}")

client.send("I'm understand".encode("utf-8"))

print("Cliend is running.")
print("Test third commit")
