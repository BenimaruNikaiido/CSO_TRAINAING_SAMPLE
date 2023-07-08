import pygatt

# Configuration du client
adapter = pygatt.GATTToolBackend()

try:
    # Démarrer l'adaptateur Bluetooth
    adapter.start()

    # Rechercher les appareils Bluetooth à proximité
    devices = adapter.scan()

    # Sélectionner l'appareil cible
    target_device = None
    for device in devices:
        if device["name"] == "Nom_de_l'appareil":
            target_device = device
            break

    # Vérifier si l'appareil cible est trouvé
    if target_device is None:
        print("Appareil cible introuvable")
        exit()

    # Se connecter à l'appareil cible
    device = adapter.connect(target_device["address"])

    # Envoyer des données au périphérique
    message = "Hello, device!"
    device.char_write("00002a00-0000-1000-8000-00805f9b34fb", message.encode())

finally:
    # Fermer la connexion avec le périphérique
    device.disconnect()

    # Arrêter l'adaptateur Bluetooth
    adapter.stop()
