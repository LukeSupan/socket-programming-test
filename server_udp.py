# CNT4704 – Analysis of Communication Networks
# UCF 2025
# Author: Prof. Al Kinoon
#
# UDP Server Program
# ------------------
# Listens on port 12000 for incoming UDP datagrams.
# For each client message:
#   1. Receives a lowercase sentence from the client.
#   2. Converts it to uppercase.
#   3. Sends the result back to the same client address/port.
# The server runs continuously until manually stopped (Ctrl+C).
#
# Protocol: UDP (connectionless, no handshake, unreliable but fast).
# Acknowledgment: Kurose & Ross (Computer Networking textbook).

from socket import *

# Assign a port number for the server
serverPort = 12000

# Create UDP socket
# AF_INET = IPv4, SOCK_DGRAM = UDP
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the socket to all interfaces on the given port
serverSocket.bind(('', serverPort))

print("The UDP server is ready to receive")

# Main loop: wait for and process client messages
while True:
    # Wait for a datagram (up to 2048 bytes)
    # Returns the message and the client’s (IP, port) tuple
    message, clientAddress = serverSocket.recvfrom(2048)
    
    # Decode bytes to string and convert to uppercase
    modifiedMessage = message.decode().upper()
    
    # Encode back to bytes and send the response to the client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
