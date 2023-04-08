import socket
import threading
import command

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 50001))

print("\n\tSERVER IS WORKING...")

def handle_client(conn, addr):
    while True:
        option = command.get_message_from_client(conn)

        if (option == "1"):
            command.create_user(conn)

        elif (option == "2"):
            command.check_account_status(conn)

        elif (option == "3"):
            command.payment_on_account(conn)

        elif (option == "4"):
            command.make_the_payment(conn)

        elif (option == "5"):
            command.transfer_money_to_account(conn)

        if (option == "q"):
            print('Server is stoped')
            break

def start():
    server.listen(0)
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(
            f'{addr} is connected\nCount of active conection {threading.active_count() - 1}\n')

print(f'server is starting...')
start()