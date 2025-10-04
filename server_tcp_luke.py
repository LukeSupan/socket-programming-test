# server_tcp_luke.py
# for CNT4704

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
    problem = connectionSocket.recv(1024).decode()

    if(problem == "0/0="):
        connectionSocket.close()
        break

    problem = problem.rstrip("=")
    
    # Parse solution into two operands and an operator
    operand1, operator, operand2 = problem.split()
    
    # Based on the operator, compute the solution
    if operator == '+':
        solution = "Answer from server: " + str(int(operand1) + int(operand2))
    elif operator == '-':
        solution = "Answer from server: " + str(int(operand1) - int(operand2))
    elif operator == '*':
        solution = "Answer from server: " + str(int(operand1) * int(operand2))
    elif operator == '/':
        solution = "Answer from server: " + str(int(operand1) / int(operand2))
    else:
        solution = "Invalid input"
    
    # Send back the modified message (encode str → bytes)
    connectionSocket.send(solution.encode())
    
    # Close this client connection
    # The main server socket (serverSocket) remains open for new clients
    connectionSocket.close()
