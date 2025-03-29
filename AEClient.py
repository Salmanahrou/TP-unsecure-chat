import msgpack  
from cryptography.fernet import Fernet  
from simple_client import SimpleClient 

class AEClient(SimpleClient):
    def __init__(self, host, send_port, broadcast_port, nick, key):
        """Initialisation du client avec chiffrement."""
        super().__init__(host, send_port, broadcast_port, nick)
        self.fernet = Fernet(key)

    def encrypt_message(self, message: str) -> bytes:
        """Chiffre un message avant de l'envoyer."""
        return self.fernet.encrypt(message.encode())

    def decrypt_message(self, encrypted_message: bytes) -> str:
        """Déchiffre un message reçu."""
        return self.fernet.decrypt(encrypted_message).decode()

    def send(self, frame: dict) -> dict:
        """Chiffre le message avant de l'envoyer."""
        frame["message"] = self.encrypt_message(frame["message"])
        return super().send(frame)
