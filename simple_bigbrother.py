import socket
import logging

# Configuration du logging pour afficher les messages
logging.basicConfig(level=logging.DEBUG)

class SimpleBigBrother:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.server_socket = None

    def start_listening(self):
        """Initialise le socket et commence à écouter les messages."""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((self.host, self.port))
        logging.info(f"BigBrother écoute sur {self.host}:{self.port}")

        while True:
            # Ecoute les messages en continu
            message, addr = self.server_socket.recvfrom(1024)
            logging.info(f"Message reçu de {addr}: {message.decode('utf-8')}")
            
            # Vous pouvez ajouter des manipulations ou des actions supplémentaires ici

    def stop_listening(self):
        """Ferme le socket si besoin."""
        if self.server_socket:
            self.server_socket.close()
            logging.info("BigBrother a arrêté d'écouter.")

if __name__ == "__main__":
    bigbrother = SimpleBigBrother('localhost', 6666)  
    bigbrother.start_listening()
