import threading
from socket import socket

def accept(server_socket):
    global clients
    while True:
        conn, address = server_socket.accept()
        clients.append(conn)


def communicate(server_socket):
    global clients
    while True:
        for client in clients:
            try:
                data = client.recv(1024).decode()
                print(data)
                for i in clients:
                    if client is not i:
                        i.send(data.encode())
            except:
                client.close()
                clients.remove(client)


def server():
    server_socket = socket()
    host = '127.0.0.1'
    port = 5000
    server_socket.bind((host, port))
    server_socket.listen(1)
    T1 = threading.Thread(target=accept, args=[server_socket])
    T2 = threading.Thread(target=communicate, args=[server_socket])
    T1.start()
    T2.start()


if __name__ == '__main__':
    clients = []
    server()
