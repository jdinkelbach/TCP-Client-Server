# Team: RGB Alphas
# Names: Justin Dinkelbach, Timothy Hinea, David Sullivan, Brandon Lee
# Date: 9/25/2020
# Project: Programming Assignment 3
# Server.py
from socket import *  # Allows creation of sockets
import threading  # Allows creation of threads


class TCPClient(threading.Thread):
    def __init__(self, port, name):
        threading.Thread.__init__(self)
        self.port = port
        self.name = name

    def run(self):
        closed = 0  # Keeps track of how many clients are closed
        while True:
            try:
                # send response once both messages are received
                if len(received) >= 2:
                    connectionSocket.send((clientOrder[0] + ": " + received[0]
                                           + " received before " + clientOrder[1] + ": " + received[1]).encode())
                # Retrieve message from client
                message = connectionSocket.recv(1024).decode()
                # Catch empty messages that are sent when user exits clients
                if message == "":
                    closed += 1;
                # Count number of closed clients
                if message == "exit" and closed < 2:
                    closed += 1
                    continue
                # when both clients are closed exit while loop
                elif closed > 1:
                    break
                else:
                    # Store message receipt order (client name)
                    clientOrder.append(self.name)
                    # Store message receipt order (message)
                    received.append(message)
                    # Print received message info
                    print("Client " + self.name + " sent message " + str(received.index(message) + 1) + ": " + message)
            except error:
                break


serverName = 'Justin-PC'  # Change this to the hostname of your PC
serverPort = 12000
# Create a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# Assign IP address and port number to socket
serverSocket.bind((serverName, serverPort))
threads = []  # Keeps track of threads
clientOrder = []  # Store client name's in message receipt order
received = []  # Store messages in receipt order
numThreads = 2

print("The server is waiting to receive 2 connections...\n")

while len(threads) < 2:
    serverSocket.listen(2)
    connectionSocket, addr = serverSocket.accept()

    # Call first client 'X'
    if 'X' not in locals():
        print("Accepted connection, calling it client X")
        connectionSocket.send("Client X connected".encode())
        X = TCPClient(serverPort, 'X')
        X.start()
        threads.append(X)

    # Call second client 'Y'
    elif 'X' in locals():
        print("Accepted connection, calling it client Y")
        connectionSocket.send("Client Y connected".encode())
        Y = TCPClient(serverPort, 'Y')
        Y.start()
        print("\nWaiting to receive messages from client X and Y\n")
        threads.append(Y)

# Wait for each thread to finish
for thread in threads:
    thread.join()
print("\nWaiting a bit for clients to close their connections....")
print("Done")
