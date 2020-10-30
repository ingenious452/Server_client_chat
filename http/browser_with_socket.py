import socket

# Name of Host and Port to connect to ->
HOST = '127.0.0.1'
PORT = 6453


def createClient():
    # creating a client socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connecting to the server
    clientSocket.connect((HOST, PORT))

    message = input('?')

    # Receiving the Data
    while message != 'q':
        # Sending Data over the network
        clientSocket.sendall(message.encode())

        # Receiving the data over network
        data = clientSocket.recv(1024).decode()

        print(f'Received from Server: {data}')
        message = input('?')

    clientSocket.close()


if __name__ == '__main__':
    createClient()
