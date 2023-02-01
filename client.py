import socket

# Set up the socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 8000))

# Send a request to the server
client_socket.send(b'REQ')

# Wait for and print the response from the server
response = client_socket.recv(1024)
print(response)

# Close the client socket
client_socket.close()
