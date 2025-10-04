# CNT4704 – Analysis of Communication Networks
# UCF 2025
# Author: Prof. Al Kinoon
#
# TCP Server Program
# ------------------
# Listens on port 12000 and waits for incoming TCP connections.
# For each client connection:
#   1. Receives one lowercase sentence.
#   2. Converts it to uppercase.
#   3. Sends the result back to the client.
#   4. Closes the connection.
# The server then loops back to wait for another client.
#
# Protocol: TCP (connection-oriented, reliable byte stream).
# Acknowledgment: Kurose & Ross (Computer Networking textbook).

from socket import *

# Create a TCP server socket
# AF_INET = IPv4, SOCK_STREAM = TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 12000

# Bind the socket to the server address and port
# '' means bind to all available network interfaces (0.0.0.0)
serverSocket.bind(('', serverPort))

# Listen for incoming connections
# Argument = backlog (max number of queued connections)
serverSocket.listen(1)

print("The server is ready to receive")

# Main server loop (runs indefinitely until manually stopped)
while True:
    # Accept a new connection from a client
    # Returns a new socket (connectionSocket) and client address info
    connectionSocket, addr = serverSocket.accept()
    
    # Receive data (up to 1024 bytes), decode from bytes → str
    sentence = connectionSocket.recv(1024).decode()
    
    # Convert message to uppercase
    capitalizedSentence = sentence.upper()
    
    # Send back the modified message (encode str → bytes)
    connectionSocket.send(capitalizedSentence.encode())
    
    # Close this client connection
    # The main server socket (serverSocket) remains open for new clients
    connectionSocket.close()
