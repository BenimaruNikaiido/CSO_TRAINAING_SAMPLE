import socket

# Configuration du serveur
host = 'localhost'
port = 8080

# Création d'un objet de type socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client_socket.connect((host, port))
print("Connected to server")

# Envoi de donnée au serveur
message = "BIENVENUE CSO!"
client_socket.send(message.encode())

# Receive the server's response
response = client_socket.recv(1024).decode()
print("Received response from server:", response)

# Close the connection
client_socket.close()
