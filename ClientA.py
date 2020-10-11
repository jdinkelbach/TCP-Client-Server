# Team: RGB Alphas
# Names: Justin Dinkelbach, Timothy Hinea, David Sullivan, Brandon Lee
# Date: 9/25/2020
# Project: Programming Assignment 3
# Client.py
# Allows creation of sockets within program
from socket import *

serverName = 'Justin-PC'  # Change this to the hostname of your PC
serverPort = 12000
message = ""
# Create a TCP socket
ClientX = socket(AF_INET, SOCK_STREAM)
# Establish connection
ClientX.connect((serverName, serverPort))
while True:
    if message == "exit":
        break
    message = ClientX.recv(1024).decode()
    if len(message) > 0:
        print("\nFrom Server: " + message + "\n")
    message = input("Enter a message to send to the server: ")
    ClientX.send(message.encode())
ClientX.close()
