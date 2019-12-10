from socket import *        # Contains everything you need to set up sockets

# Create destination server name and server port to send message to
server_name = '127.0.0.1'       # This can be a website URL! DNS lookup happens automatically, very cool
server_port = 400               # Port address is the socket address on the server

# Create a socket for the client. Uses IPV4.
client_socket = socket(AF_INET, SOCK_DGRAM)     # SOCK_DGRAM indicates UDP

# Create a message to send to the server
message = raw_input('Input a number to check if it is prime: ')        # Data comes from console input

# Attach destination server name and server port to message and send the message on its way
client_socket.sendto(message, (server_name, server_port))

# Now wait for message to come from server
result, server_address = client_socket.recvfrom(2048)     # server_address contains server's IP address and port number; 2048 is buffer size

# Print message
print "From server: ", result

# Close socket and terminate process
client_socket.close()
