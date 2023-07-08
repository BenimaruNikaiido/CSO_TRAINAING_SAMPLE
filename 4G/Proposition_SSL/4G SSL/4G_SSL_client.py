import socket
import ssl

def run_client():
    host = '127.0.0.1'
    port = 8080

    context = ssl.create_default_context()

    with socket.create_connection((host, port)) as client_socket:
        client_socket = context.wrap_socket(client_socket, server_hostname=host)
        print(f"Connexion établie avec le serveur {host}:{port}")

        try:
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
