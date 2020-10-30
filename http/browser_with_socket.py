import socket

# Name of Host and Port to connect to ->
HOST = '127.0.0.1'
PORT = 6453


def createClient():
    # creating a client socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connecting to the server
    clientSocket.connect((HOST, PORT))
    print('Client Active'.center(20, '-'))

    message = input('->')

    # Receiving the Data
    while message != 'q':
        # Sending Data over the network
        clientSocket.sendall(message.encode())

        # Receiving the data over network
        data = clientSocket.recv(1024).decode()

        print(f'From connected server: {data}')
        message = input('->')

    clientSocket.close()
    print('Client Closed'.center(20, '-'))


if __name__ == '__main__':
    createClient()
