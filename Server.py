# Team: RGB Alphas
# Names: Justin Dinkelbach, Timothy Hinea, David Sullivan, Brandon Lee
# Date: 9/25/2020
# Project: Programming Assignment 3
# Server.py
# Allows creation of sockets within program
from socket import *
import threading


class TCPClient(threading.Thread):
    def __init__(self, port, name):
        threading.Thread.__init__(self)
        self.port = port
        self.name = name

    def run(self):
        count = 1
        while True:
            # Retrieve and send message from client
            message = connectionSocket.recv(1024).decode()
            if message == "exit":
                break
            print("Client " + self.name + " sent message " + str(count) + ": " + message)
            clientOrder.append(self.name)
            messageOrder.append(message)
            count += 1
serverPort = 12000
# Create a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
# Assign IP address and port number to socket
serverSocket.bind(('', serverPort))
threads = []        # Keeps track of threads
clientOrder = []
messageOrder = []
serverMessage = ""
numThreads = 2
names = ['X', 'Y']  # t1 = X, t2 = Y
print("The server is waiting to receive 2 connections...\n")

while True:
    serverSocket.listen(2)
    connectionSocket, addr = serverSocket.accept()
    if 'X' not in locals():
        print("Accepted connection, calling it client X")
        connectionSocket.send("Client X connected".encode())
        X = TCPClient(serverPort, 'X')
        X.start()
        threads.append(X)
    else:
        print("Accepted connection, calling it client Y")
        connectionSocket.send("Client Y connected".encode())
        Y = TCPClient(serverPort, 'Y')
        Y.start()
        threads.append(Y)
        print("\nWaiting to receive messages from client X and Y\n")

connectionSocket.send(("Client " + clientOrder.pop(0) + ": " + messageOrder.pop(0)
                       + "received before " + clientOrder.pop() + ": " + messageOrder.pop()).encode())
print("\nWaiting a bit for clients to close their connections.")
# Wait for each thread to finish
for thread in threads:
    thread.join()
print("Done")
