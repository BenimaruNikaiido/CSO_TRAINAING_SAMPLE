import pygatt

# UUID de la caractéristique
char_uuid = "00002a00-0000-1000-8000-00805f9b34fb"

# Configuration du serveur
adapter = pygatt.GATTToolBackend()

def handle_data(handle, value):
    print("Données reçues :", value.decode())

try:
    # Démarrer l'adaptateur Bluetooth
    adapter.start()

    # Rechercher les appareils Bluetooth à proximité
    devices = adapter.scan()

    # Sélectionner le périphérique cible
    target_device = None
    for device in devices:
        if device["name"] == "Nom_de_l_appareil":
            target_device = device
            break

    # Vérifier si le périphérique cible est trouvé
    if target_device is None:
        print("Périphérique cible introuvable")
        exit()

    # Se connecter au périphérique cible
    device = adapter.connect(target_device["address"])
    print("Connecté au périphérique :", target_device["name"])

    # Activer la notification pour la caractéristique
    device.subscribe(char_uuid, callback=handle_data)

    # Garder le programme en cours d'exécution indéfiniment
    input("Appuyez sur EntréeJe m'excuse pour les erreurs précédentes. Voici le code corrigé pour le client et le serveur Bluetooth 5 utilisant la bibliothèque PyGATT :

**Serveur Bluetooth 5 :**

```python
import pygatt

# UUID de la caractéristique
char_uuid = "00002a00-0000-1000-8000-00805f9b34fb"

def handle_data(handle, value):
    print("Données reçues :", value.decode())

# Configuration du serveur
adapter = pygatt.GATTToolBackend()

try:
    # Démarrer l'adaptateur Bluetooth
    adapter.start()

    # Rechercher les appareils Bluetooth à proximité
    devices = adapter.scan()

    # Sélectionner le périphérique cible
    target_device = None
    for device in devices:
        if device["name"] == "Nom_de_l_appareil":
            target_device = device
            break

    # Vérifier si le périphérique cible est trouvé
    if target_device is None:
        print("Périphérique cible introuvable")
        exit()

    # Se connecter au périphérique cible
    device = adapter.connect(target_device["address"])
    print("Connecté au périphérique :", target_device["name"])

    # Activer la notification pour la caractéristique
    device.subscribe(char_uuid, callback=handle_data)

    # Garder le programme en cours d'exécution indéfiniment
    input("Appuyez sur Entrée pour arrêter le serveur...\n")

finally:
    # Se désabonner de la caractéristique
    device.unsubscribe(char_uuid)

    # Fermer la connexion avec le périphérique
    device.disconnect()

    # Arrêter l'adaptateur Bluetooth
    adapter.stop()
