# python 3.7
# multithread server

#------------------------
import socket
import sys

# importing the threading module
from _thread import *
import threading
# -------------------

# define thread object
lockThread = threading.Lock()
#--------------------

def multipleConnection(clientSocket, address):

    # transfering the data and retreiving it
    while True:
        try:
            response = clientSocket.recv(1024).decode('utf-8')

            # check if data there is response or not
            if not response:
                listOfClients.remove(clientSocket)
                lockThread.release()
                break

            else:
                message = f'From {address[0]: {response}}'
                broadcast(clientSocket, message)

        except:
            continue

    clientSocket.close()
    print('client went OFFLINE'.center(50, '-'))

    def broadcastMessage(connection, msg):
        # loop through list of client in room and send message to everyone
        for client in listOfClients:
            if connection != client:
                try:
                    client.sendall(msg.encode('utf-8'))
                except:
                    client.close()
                    remove(client)

    def removeClient(c):
        if client in listOfClients:
            listOfClients.remove(c)
# ---------------------------------------------------


listOfClients = list()


def createServer():
    # host and port address of the server
    host = '127.0.0.1'
    port = 6453

    # creating a server side socket
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # bind the server socket with the given address
    try:
        serverSocket.bind((host, port))
    except socket.error as e:
        print(f'Unable to find the socket with address Error: {e}')
        sys.exit()

    # server listening for connection with maximum hold of 5
    serverSocket.listen(5)
    print('Chatroom Acitvated'.center(50, '-'))

    while True:
        # accepting connection
        (connectionSocket, address) = serverSocket.accept()
        # append the client in list of client
        listOfClients.append(connectionSocket)

        print(f'\nJoin the meeting: {address[0]}')

        # acquire thread lock
        lockThread.acquire()

        # pass the connection to the
        start_new_thread(multipleConnection, (connectionSocket, address))

    serverSocket.close()
# ---------------------------------------------------


if __name__ == '__main__':
    createServer()
