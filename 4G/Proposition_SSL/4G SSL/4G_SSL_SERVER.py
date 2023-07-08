import socket
import ssl

def run_server():
    host = '0.0.0.0'
    port = 8080

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile='server.crt', keyfile='server.key')

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Le serveur est à l'écoute sur {host}:{port}")

        with context.wrap_socket(server_socket, server_side=True) as ssl_server_socket:
            while True:
                client_socket, client_address = ssl_server_socket.accept()
                print(f"Connexion établie avec {client_address[0]}:{client_address[1]}")

                try:
                    data = client_socket.recv(1024)
                    received_data = data.decode().strip()
                    print(f"Message reçu du client : {received_data}")

                    if received_data == "Hello, server!":
                        response = "Message reçu avec succès!"
                        client_socket.send(response.encode())
                    else:
                        response = "Requête non autorisée!"
                        client_socket.send(response.encode())
                except socket.error as e:
                    print(f"Une erreur s'est produite lors du traitement de la requête : {str(e)}")
                    response = "Une erreur s'est produite lors du traitement de votre requête."
                    client_socket.send(response.encode())
                except Exception as e:
                    print(f"Une exception s'est produite : {str(e)}")

                client_socket.close()

if __name__ == '__main__':
    run_server()
