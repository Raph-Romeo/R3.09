import threading, sys
from socket import socket
from validators import ipv4

# CLIENT


def connect():
    print('--- CONNECT TO SOCKET ---')
    ip = input('Insert IP address: ')
    while not ipv4(ip):
        ip = str(input('Please insert valid IP address (A.B.C.D): '))
    port = int(input(f"Insert the socket's port {ip}:"))
    client_socket = socket()
    try:
        client_socket.connect((ip, port))
    except:
        print('There was an error while connecting to socket')
        sys.exit(-1)
    else:
        print('Connection was a success.')
        return client_socket


def disconnect(client_socket):
    global stop_threads
    client_socket.close()
    stop_threads = True

def recieve(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        print(data)
        if stop_threads:
            break


def write(client_socket, username):
    while True:
        try:
            msg = input(f"{username}> ")
            if msg == '/disconnect':
                disconnect(client_socket)
            else:
                message =f'{username}> {msg}'
                client_socket.send(message.encode())
        except:
            disconnect(client_socket)
            sys.exit(-2)
        if stop_threads:
            break


def main():
    username = input('Insert username: ')
    client_socket = connect()
    T1 = threading.Thread(target=write, args=[client_socket, username])
    T2 = threading.Thread(target=recieve, args=[client_socket])
    T1.start()
    T2.start()
    T1.join()
    T2.join()
    print('Successfully disconnected from socket')
    sys.exit(0)


if __name__ == '__main__':
    threads = []
    stop_threads = False
    main()
