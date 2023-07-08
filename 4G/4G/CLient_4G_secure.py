import socket

def run_client():
    host = '127.0.0.1'
    port = 8080

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((host, port))
            print(f"Connexion établie avec le serveur {host}:{port}")

            message = "Hello, server!"
            client_socket.send(message.encode())

            data = client_socket.recv(1024)
            received_data = data.decode().strip()

            if received_data == "Message reçu avec succès!":
                print("Réponse du serveur :", received_data)
            else:
                print("Requête non autorisée !")
        except ConnectionRefusedError:
            print(f"Impossible de se connecter au serveur {host}:{port}")
        except socket.error as e:
            print(f"Une erreur s'est produite lors de la communication avec le serveur : {str(e)}")
        except Exception as e:
            print(f"Une exception s'est produite : {str(e)}")

if __name__ == '__main__':
    run_client()
