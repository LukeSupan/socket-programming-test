# client_tcp_luke.py
# for CNT4704

from socket import *

# Define server address and port
serverName = "eustis3.eecs.ucf.edu"   # Use "localhost" when client and server are on same machine
serverPort = 10400         # Must match the server’s listening port

while True:

    # Create socket called clientSocket and establish a TCP connection with the server
    # AF_INET = IPv4, SOCK_STREAM = TCP protocol
    clientSocket = socket(AF_INET, SOCK_STREAM)

    # Initiate TCP connection (3-way handshake with server)
    # The OS assigns a local ephemeral port automatically
    clientSocket.connect((serverName, serverPort))

    # Prompt user for input (math problem a+b=)
    problem = input('Input math problem: ')

    # Send the input string to the server, converting from string → bytes
    clientSocket.send(problem.encode())

    # Exit condition, close the socket and break the loop
    if problem == "0/0=":
        clientSocket.close()
        break

    # Wait to receive up to 1024 bytes from the server
    # recv() blocks until data arrives or connection closes
    solution = clientSocket.recv(1024)

    # Decode server’s response (bytes → str) and display
    print('From Server:', solution.decode())

    # Close the client socket after each problem
    clientSocket.close()