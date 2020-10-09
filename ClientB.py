# Team: RGB Alphas
# Names: Justin Dinkelbach, Timothy Hinea, David Sullivan, Brandon Lee
# Date: 9/25/2020
# Project: Programming Assignment 3
# Client.py
# Allows creation of sockets within program
from socket import *


serverName = 'Justin-PC'
serverPort = 12000
message = ""

ClientY = socket(AF_INET, SOCK_STREAM)
ClientY.connect((serverName, serverPort))

while message != "exit":
    message = ClientY.recv(1024).decode()
    if len(message) > 0:
        print("From Server: " + message)
    message = input("Enter a message to send to the server: ")
    ClientY.send(message.encode())
ClientY.close()
