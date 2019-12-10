from socket import *       # Contains everything you need to set up sockets
from Prime import is_prime

# Create server port address and socket
server_port = 400
server_socket = socket(AF_INET, SOCK_DGRAM)     # Uses IPV4. SOCK_DGRAM indicates UDP

# Assign the port number server_port to the server's socket
server_socket.bind(('', server_port))

print "The server is ready to receive..."

# While loop to continuously to constantly be available for messages
while 1:
    # Store message and client address
    message, client_address = server_socket.recvfrom(2048)

    # Check if message is prime
    num_to_check = int(message)     # Cast data to integer

    if is_prime(num_to_check):
        result = "Number is prime! :-)"
    else:
        result = "Number is NOT prime. :-("

    # Send message back to client using client address
    server_socket.sendto(result, client_address)
