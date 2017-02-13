#!/usr/bin/python3

"""
Simple HTTP Server
Jesus M. Gonzalez-Barahona and Gregorio Robles
{jgb, grex} @ gsyc.es
TSAI, SAT and SARO subjects (Universidad Rey Juan Carlos)
"""

import random
import socket

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 8080))

# Queue a maximum of 5 TCP connection requests

mySocket.listen(5)

# La IP esta alojada en la posicion 1 de address.
# El Puerto esta alojado en la possicion 2 de address.

while True:
	print ('Waiting for connections')
	(recvSocket, address) = mySocket.accept()
	numero_random = random.randint(0,10000000)
	print ('HTTP request received:')
	print (recvSocket.recv(1024))
	recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
			"<html><body><h1>Hola. <a href= http://localhost:8080/"+str(numero_random)+">Dame otra''</a></h1></body></html>" +
			"\r\n", "utf-8"))
	recvSocket.close()
