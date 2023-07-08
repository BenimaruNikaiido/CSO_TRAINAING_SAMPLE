# CSO_TRAINING_SAMPLE
INTRODUCTION A L'INGENIEURIE RM &amp; IoT![IoT](https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/assets/138717853/d14f8641-27a7-46c5-bfbb-af085bb5f46d)

# PLAN 
![200 (1)](https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/assets/138717853/abbf1e7d-e5ea-4c90-be0f-47d73b8017ab)



# PRESENTATION DU PROTOCOLE 4G
![rocket](https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/assets/138717853/1a6fb7a0-009c-4531-aae0-23693e1cf82a)

**Le protocole 4G (quatrième génération) est une norme de communication sans fil pour les réseaux 
mobiles qui a été développée pour succéder au protocole 3G (troisième génération). Il a été conçu pour 
fournir des performances améliorées en termes de vitesse de transfert de données, de capacité du 
réseau, de qualité de service et de fiabilité de la connexion**

Voici quelques caractéristiques clés du protocole 4G :

- Haute vitesse de transmission de données 
- Capacité réseau améliorée
- Qualité de service (QoS) améliorée
- Fiabilité de la connexion
- Utilisation d'IPv6
- Applications et services

Code source en python client-serveur 4G

La mise en place d'un serveur 4G complet nécessite un accès à une infrastructure de réseau mobile 4G 
et l'utilisation de protocoles spécifiques fournis par le fournisseur de services. Cependant, voici un 
exemple de code Python pour un client et un serveur simulé utilisant le module socket pour établir 
une connexion TCP :

Serveur 4G (simulé) voir lien ci dessous

https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/blob/main/4G/CODE%20SOURCE%20SERVEUR%204G%20SIMULE.JPG

### OBSERVATION

Les principales failles de sécurité potentielles dans le code source par défaut sont les suivantes :

- **Le serveur ne procède pas à la validation ni au filtrage des données d'entrée** : les données du client sont reçues et traitées directement par le serveur sans validation ni filtrage. Cela pourrait conduire à des attaques par injection de code, dans lesquelles un attaquant pourrait transmettre des données malveillantes pour exploiter des vulnérabilités potentielles.

- **Le manque de gestion des exceptions particulières** : Toutes les exceptions génériques sont capturées par le bloc `try-except` actuel, ce qui peut rendre le serveur vulnérable à des attaques où un attaquant tente de provoquer des erreurs ou des comportements inattendus pour exploiter une faille.

- **Le code ne vérifie pas l'identité ou l'authenticité du client qui se connecte** : Cela signifie que n'importe qui peut se connecter au serveur sans avoir besoin d'authentification, permettant à des utilisateurs non autorisés d'accéder ou de manipuler des données sensibles.

- **Le serveur ne dispose pas de mécanismes de protection contre les attaques de déni de service (DoS) ou de détection d'activités anormales** : Cela peut rendre le serveur vulnérable à une attaque où un attaquant tente de saturer les ressources du serveur et de le rendre indisponible pour les autres utilisateurs.

- **Aucune sécurité ou chiffrement des communications** : le code ne met pas en place de mécanismes de sécurité ou de chiffrement des communications. Cela signifie que des tiers peuvent intercepter ou manipuler les données échangées entre le client et le serveur.

_Il est conseillé d'appliquer des mesures de sécurité telles que la validation et le filtrage des données d'entrée, la gestion appropriée des exceptions, la mise en place de contrôles d'authentification, la protection contre les attaques de déni de service et l'utilisation de protocoles de chiffrement pour sécuriser les communications afin de renforcer la sécurité du code._

### MODIFICATION APPORTEE DANS LE CODE : cas du serveur                                       


![FICHIER_4G_SECURE](https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/assets/138717853/06c89f57-c1ab-4d03-acc7-ab3f79f66386)                       ![code-coding](https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/assets/138717853/e3fa1aed-cd98-4fb8-86d3-6c67a8c36d66)

**NB** : (voir fichier dossier 4G pour le client)

# PRESENTATION DU PROTOCOLE BLUETOOTH 5
![bluetooth-hacking](https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/assets/138717853/1666eaf7-2fa6-4687-b1c6-9e0a93adb21a)

**Le Bluetooth 5.0 est la cinquième génération de la technologie Bluetooth, qui est largement utilisée pour connecter divers appareils électroniques sans fil. Cette mise à jour a été officiellement lancée en décembre 2016. Comparé à ses prédécesseurs, le Bluetooth 5.0 offre des améliorations significatives en termes de vitesse, de portée et de capacité de données**

### Les principales améliorations du Bluetooth 5.0 ###

Voici les principales améliorations apportées par le Bluetooth 5.0 par rapport aux versions précédentes :

- **Portée accrue** : Le Bluetooth 5.0 offre une portée quatre fois supérieure à celle du Bluetooth 4.2, ce qui signifie qu’il peut atteindre jusqu’à 240 mètres en théorie, bien que la portée réelle puisse varier en fonction de l’environnement et des dispositifs utilisés.
- **Vitesse de transmission améliorée** : La vitesse de transmission des données du Bluetooth 5.0 est deux fois plus rapide que celle du Bluetooth 4.2, atteignant jusqu’à 2 Mbits/s.
- **Capacité de données** : Le Bluetooth 5.0 peut transmettre huit fois plus de données par paquet que le Bluetooth 4.2, ce qui permet une meilleure qualité audio et une connexion plus stable.
- **Compatibilité** : Le Bluetooth 5.0 est rétrocompatible avec les versions précédentes du Bluetooth, ce qui signifie qu’il peut fonctionner avec des dispositifs utilisant des versions antérieures de la technologie.

### CODE SOURCE SIMULE BLUETOOTH 5 ###

![SERVEUR BLUETTOTH 5](https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/assets/138717853/e632c486-2d22-4095-bdbc-48f0bc22e004)

NB : (voir suite dans dossier BLUETOOTH 5 pour le client et serveur + modification apportées via ce lien https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/tree/main/BLUETOOTH%205

![code-coding](https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/assets/138717853/d0fa667a-b421-4774-861e-71cc1a27cfb8)
https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/blob/main/BLUETOOTH%205/SERVEUR_BLUETOOTH_MAIN.py.py

# PRESENTATION DU PROTOCOLE IMAP
![IMAP-מה-זה](https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/assets/138717853/e30cf4ea-3b1b-4495-b4b7-35a1cda4cf93)

**L’IMAP (Interactive Mail Access Protocol) est un protocole qui vous permet, depuis un programme (logiciel ou application) installé sur votre ordinateur ou votre smartphone, d’accéder aux messages de votre boîte aux lettres électronique**

### En quoi consiste le protocole IMAP ? ###

Les courriers électroniques qui atterrissent dans notre boîte de réception ne peuvent être manipulés sans un protocole spécifique, l’IMAP. Ce terme est, en fait, l’abréviation d’Internet Message Access Protocol. Il s’agit d’un protocole standard de récupération des messages entrants. C’est par ce protocole qu’on peut manipuler à volonté les courriels dans la boîte de réception. L’IMAP stocke les messages sur un serveur de messagerie pour permettre au destinataire de les afficher et de les archiver comme avec les fichiers conservés sur un appareil local.

CODE SOURCE IMAP SIMULEE (https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/blob/main/IMAP/IMAP%20SERVER%20CODE%20SOURCE.JPG)

### OBSERVATION ###
https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/blob/main/IMAP/IMAP%20OBSERVATION.JPG
https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/blob/main/IMAP/IMAP%20OBSERVATION%202.JPG

### MOODIFICATION APPORTEES ###

### EXECUTION DU CODE ### 
![code-coding](https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/assets/138717853/64945791-6ebc-4ad5-8b2d-9d99bbf04403)

https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/blob/main/IMAP/SERVER_IMAP_SOURCE.py
https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/blob/main/IMAP/IMAP%20SERVEUR%20PYTHON.JPG



![8BtJ](https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/assets/138717853/09aa9bec-28f6-42b3-b56d-0571a2ad947e) ![ElegantMaleCero-size_restricted](https://github.com/kaoscomputing/CSO_TRAINAING_SAMPLE/assets/138717853/c7454e76-26a8-4c63-8d22-373c2d034c25)
