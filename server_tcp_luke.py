# server_tcp_luke.py
# for CNT4704

from socket import *

# Create a TCP server socket
# AF_INET = IPv4, SOCK_STREAM = TCP
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign a port number
serverPort = 10400

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

    # 0/0= is exit condition
    if(problem == "0/0="):
        break
    
    # Get rid of the = for splitting
    problem = problem.rstrip("=")
    
    # Split the problem around the operator
    for foundOperator in "+-*/":
        if foundOperator in problem:
            operand1, operand2 = problem.split(foundOperator)
            operator = foundOperator
            break
    
    # Based on the operator, compute the solution. If the problem is invalid (divide by 0, return input error)
    if operator == '+':
        solution = "Answer from server: " + str(float(operand1) + float(operand2))
    elif operator == '-':
        solution = "Answer from server: " + str(float(operand1) - float(operand2))
    elif operator == '*':
        solution = "Answer from server: " + str(float(operand1) * float(operand2))
    elif operator == '/':
        if float(operand2) == 0:
            solution = "Input error. Re-type the math question again"
        else:
            solution = "Answer from server: " + str(float(operand1) / float(operand2))
    else:
        solution = "Input error. Re-type the math question again"
    
    # Send back the modified message (encode str → bytes)
    connectionSocket.send(solution.encode())
    
    # Close this client connection
    # The main server socket (serverSocket) remains open for new clients
    connectionSocket.close()

# Close sockets after breaking the loop
connectionSocket.close()
serverSocket.close()
