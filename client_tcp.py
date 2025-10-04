# CNT4704 – Analysis of Communication Networks
# UCF 2025
# Author: Prof. Al Kinoon
#
# TCP Client Program
# ------------------
# This client sends a lowercase string to a TCP server.
# The server receives it, converts the string to uppercase,
# and sends it back. The client prints the server’s response
# and then terminates the connection.
#
# Protocol: TCP (connection-oriented, reliable byte stream).
# Acknowledgment: Kurose & Ross (Computer Networking textbook).

from socket import *

# Define server address and port
serverName = "localhost"   # Use "localhost" when client and server are on same machine
serverPort = 12000         # Must match the server’s listening port

# Create socket called clientSocket and establish a TCP connection with the server
# AF_INET = IPv4, SOCK_STREAM = TCP protocol
clientSocket = socket(AF_INET, SOCK_STREAM)

# Initiate TCP connection (3-way handshake with server)
# The OS assigns a local ephemeral port automatically
clientSocket.connect((serverName, serverPort))

# Prompt user for input (one sentence in lowercase)
sentence = input('Input math problem: ')

# Send the input string to the server, converting from int → bytes
clientSocket.send(sentence.encode())

# Wait to receive up to 1024 bytes from the server
# recv() blocks until data arrives or connection closes
solvedProblem = clientSocket.recv(1024)

# Decode server’s response (bytes → str) and display
print('From Server:', solvedProblem.decode())

# Close the socket
# This sends a FIN to the server to gracefully terminate the connection
clientSocket.close()
