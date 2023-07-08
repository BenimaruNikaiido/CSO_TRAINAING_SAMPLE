import socket
import tkinter as tk

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

# Set up a Tkinter window for displaying the message
window = tk.Tk()
window.title("Server Status")
window.geometry("300x100")
status_label = tk.Label(window, text="Waiting for clients...", font=("Arial", 12))
status_label.pack()

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

    # Update the status label
    status_label.config(text=f"Connected clients: {connected_clients}")

    # Check if the maximum number of clients is reached
    if connected_clients >= 5:
        status_label.config(text="NOMBRE D'UTILISATEURS MAX ATTEINT", fg="green", font=("Arial Black", 20))
        break

# Close the server socket
server_socket.close()

# Run the Tkinter event loop
window.mainloop()
