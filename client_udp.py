# CNT4704 – Analysis of Communication Networks
# UCF 2025
# Author: Prof. Al Kinoon
#
# UDP Client Program
# ------------------
# This client sends a lowercase string to a UDP server.
# The server receives it, converts the string to uppercase,
# and sends it back. The client prints the server’s response
# and then terminates.
#
# Protocol: UDP (connectionless, no handshake, unreliable but fast).
# Acknowledgment: Kurose & Ross (Computer Networking textbook).

from socket import *

# Define server address and port
serverName = "localhost"   # Use "localhost" when client and server are on same machine
serverPort = 12000         # Must match the server’s listening port

# Create UDP socket (AF_INET = IPv4, SOCK_DGRAM = UDP)
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Prompt user for input (one sentence in lowercase)
message = input('Input lowercase sentence:')

# Send message to the server at (serverName, serverPort)
# sendto() requires both the data and destination address
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Wait for server’s reply (up to 2048 bytes)
# recvfrom() returns the response data and the server’s address tuple
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# Decode and print the server’s response
print(modifiedMessage.decode())

# Close the socket (client is done)
clientSocket.close()
