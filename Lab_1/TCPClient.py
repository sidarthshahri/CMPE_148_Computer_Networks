from socket import *        # Here's where all the socket goodies come from

# Define destination server name and port address to interface with
server_name = '127.0.0.1'
server_port = 12000

# Set up client socket. Will be used to talk to TCP server
client_socket = socket(AF_INET, SOCK_STREAM)    # Uses IPV4. SOCK_STREAM indicates TCP

# A TCP connection (like a pipe) must be established with the server before proceeding
client_socket.connect((server_name, server_port))

# Get data from console input to send to server
number = raw_input('Input number to check if prime: ')

# Send data to server using previous connection
client_socket.send(number)

# Wait for data to be received from server
result = client_socket.recv(2048)        # 2048 is buffer size

# Print data received from server
print 'From server:', result

# Close socket connection
client_socket.close()
