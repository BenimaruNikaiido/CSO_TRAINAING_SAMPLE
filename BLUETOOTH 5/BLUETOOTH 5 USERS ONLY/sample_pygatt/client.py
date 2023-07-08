from gatt import *

# UUID de la caractéristique
char_uuid = "00002a00-0000-1000-8000-00805f9b34fb"

# Créer une instance du backend
backend = GATTToolBackend()

try:
    # Démarrer le backend
    backend.start()

    # Créer un client
    client = ClientManager(backend)

    # Rechercher les appareils Bluetooth à proximité
    client.discover()

    # Sélectionner l'appareil cible
    target_device = client.device(name="Nom_de_l_appareil")

    if target_device is None:
        print("Appareil cible introuvable")
        exit()

    # Créer une instance du périphérique client
    device = client.device(mac_address=target_device.mac_address)

    # Se connecter à l'appareil cible
    device.connect()

    # Envoyer des données au périphérique
    message = "Hello, device!"
    device.char_write(char_uuid, bytearray(message, 'utf-8'))

finally:
    # Fermer la connexion avec le périphérique
    device.disconnect()

    # Arrêter le backend
    backend.stop()
