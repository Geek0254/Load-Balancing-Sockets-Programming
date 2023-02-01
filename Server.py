import socket

# Set up the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 8000))
server_socket.listen()

# Set up load balancing variables
server1_request_count = 0
server2_request_count = 0

# Wait for and handle client requests
while True:
    client_socket, client_address = server_socket.accept()

    # Load balance between the two servers
    if server1_request_count < 3:
        # Handle the request using server1
        server1_request_count += 1
        print(f'Handling request from {client_address} using server1')
    elif server2_request_count < 3:
        # Handle the request using server2
        server2_request_count += 1
        print(f'Handling request from {client_address} using server2')
    else:
        # Handle the request using either server1 or server2
        if server1_request_count < server2_request_count:
            server1_request_count += 1
            print(f'Handling request from {client_address} using server1')
        else:
            server2_request_count += 1
            print(f'Handling request from {client_address} using server2')

    # Send a response to the client
    client_socket.send(b'ACK')

    # Close the client socket
    client_socket.close()
