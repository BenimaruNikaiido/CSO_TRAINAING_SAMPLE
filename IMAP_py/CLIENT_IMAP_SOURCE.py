import ssl
from imaplib import IMAP4

# Configuration du client IMAP
host = 'localhost'
port = 143
username = 'your_username'
password = 'your_password'

# Création d'une instance du client IMAP
client = IMAP4(host, port)

# Configuration de la connexion SSL/TLS
client.starttls(context=ssl.create_default_context(ssl.Purpose.CLIENT_AUTH))

# Connexion au serveur IMAP
client.login(username, password)

# Liste des boîtes aux lettres disponibles
response, mailbox_list = client.list()
print(f"Boîtes aux lettres disponibles :")
for mailbox in mailbox_list:
    print(mailbox.decode())

# Sélection d'une boîte aux lettres
mailbox_name = 'INBOX'
client.select(mailbox_name)

# Récupération des en-têtes des e-mails
response, message_ids = client.search(None, 'ALL')
for message_id in message_ids[0].split():
    response, header_data = client.fetch(message_id, '(BODY.PEEK[HEADER])')
    header = header_data[0][1].decode()
    print(f"En-tête de l'e-mail {message_id.decode()}:")
    print(header)

# Déconnexion du serveur IMAP
client.logout()
