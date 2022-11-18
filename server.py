import threading
from socket import socket
import sys


def accept(server_socket):
    global clients
    while True:
        conn, address = server_socket.accept()
        clients.append(conn)
        threading.Thread(target=communicate, args=[conn]).start()


def communicate(client):
    global clients
    while True:
        try:
            data = client.recv(1024).decode()
            print(data)
            for i in clients:
                if client is not i:
                    i.send(data.encode())
        except:
            client.close()
            clients.remove(client)
            print('server > Disconnected client')
            sys.exit()


def server():
    server_socket = socket()
    host = '127.0.0.1'
    port = 5000
    server_socket.bind((host, port))
    server_socket.listen(10)
    T1 = threading.Thread(target=accept, args=[server_socket])
    T1.start()


if __name__ == '__main__':
    clients = []
    server()
