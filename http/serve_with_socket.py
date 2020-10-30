import socket


HOST = '127.0.0.1'
PORT = 6453

def createServer():

    # create an server socket object
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # binding the object to the address
    serverSocket.bind((HOST, PORT))

    # listening to the connection request with blocking
    serverSocket.listen(5)
    print(f'Server: {HOST}'.center(50, '-'))

    # Establishing  connection --------

    # accepting the connection request
    # returning a client socket object
    (clientSocket, address) = serverSocket.accept()
    print(f'Connection from: {address}')
    #-------------------------

    # Receiving data------------
    while True:
        # data received is in utf8 and need to be decode to string
        data = clientSocket.recv(1024).decode()
        # checking if all data has been transfered
        if len(data) < 1:
            break
        print(f'From connected user: {data}')

        data = input('->')
        clientSocket.sendall(data.encode())

    clientSocket.close()
    print('Server Closed'.center(50, '-'))


if __name__ == '__main__':
    createServer()
