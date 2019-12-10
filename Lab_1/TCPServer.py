from socket import *            # Socket goodies
from Prime import is_prime

# Set up server port address and socket
server_port = 12000
server_socket = socket(AF_INET, SOCK_STREAM)        # SOCK_STREAM indicates TCP

# Bind the server port address to the socket to give it an identity
server_socket.bind(('', server_port))

# Tells socket to listen for TCP connection requests from the client
server_socket.listen(1)     # Maximum number of connections given by parameter "1"

print "The server is ready to receive"

while 1:
    # Creates another socket dedicated for the pipe between client and server
    connection_socket, client_address = server_socket.accept()

    # Store data from client
    number = connection_socket.recv(1024)

    # Cast number to an int
    number = int(number)

    # Check if number from client is prime
    if is_prime(number):
        result = "Number is prime! :-)"
    else:
        result = "Number is NOT prime. :-("

    # Send data back to client
    connection_socket.send(result)

    # Close pipe connection between client and server. Note that the server can still accept new connections from the
    # initial socket
    connection_socket.close()
