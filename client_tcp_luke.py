# client_tcp_luke.py
# for CNT4704

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
problem = input('Input math problem: ')

# Send the input string to the server, converting from string → bytes
clientSocket.send(problem.encode())

# Wait to receive up to 1024 bytes from the server
# recv() blocks until data arrives or connection closes
solution = clientSocket.recv(1024)

# Decode server’s response (bytes → str) and display
print('From Server:', solution.decode())

# Close the socket
# This sends a FIN to the server to gracefully terminate the connection
clientSocket.close()
