import socket
import pygatt

# Server configuration
host = 'localhost'
port = 8080

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

print("Server listening on {}:{}".format(host, port))

# Accept a client connection
client_socket, client_address = server_socket.accept()
print("Connected to client:", client_address)

# Bluetooth configuration
adapter = pygatt.GATTToolBackend()
adapter.start()

# Discover nearby Bluetooth devices
devices = adapter.scan()

# Select the target device
target_device = None
for device in devices:
    if device["name"] == "Nom_de_l'appareil":
        target_device = device
        break

# Check if the target device is found
if target_device is None:
    print("Target device not found")
    client_socket.close()
    server_socket.close()
    exit()

# Connect to the target device
device = adapter.connect(target_device["address"])

# Read data from the Bluetooth device
data = device.char_read("00002a00-0000-1000-8000-00805f9b34fb")
received_data = data.decode()
print("Received data from Bluetooth device:", received_data)

# Send a response back to the client
response = "Hello from the server and Bluetooth device: " + received_data
client_socket.send(response.encode())

# Close the connection
device.disconnect()
adapter.stop()
client_socket.close()
server_socket.close()
