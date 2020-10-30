# python 3.7
# client side socket

import socket
import select
import sys


def createClient():
    host = '127.0.0.1'
    port = 6453

    # create client socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect to the server
    clientSocket.connect((host, port))

    # recieve message from the server
    message = input(' -> ')

    # Transfer and Recieve data
    while message != 'q':
        if sock == clientSocket:
            message = clientSocket.recv(1024).decode('utf-8')
            print(message)
        else:
            message = input('  ->  ')
            clientSocket.sendall(message)

    clientSocket.close()


if __name__ == '__main__':
    createClient()
