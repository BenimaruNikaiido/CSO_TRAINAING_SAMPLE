import socket

# Server configuration
host = 'localhost'
port = 8080

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print("Server listening on {}:{}".format(host, port))

# Count the number of connected clients
connected_clients = 0

while connected_clients < 5:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print("Connected to client:", client_address)

    # Receive data from the client
    data = client_socket.recv(1024).decode()
    print("Received data from client:", data)

    # Send a response back to the client
    response = "Hello from the server!"
    client_socket.send(response.encode())

    # Close the connection
    client_socket.close()

    # Update the number of connected clients
    connected_clients += 1

    # Check if the maximum number of clients is reached
    if connected_clients >= 5:
        print("\033[92mNOMBRE D'UTILISATEURS MAX ATTEINT\033[0m")  # Afficher en vert

# Close the server socket
server_socket.close()
