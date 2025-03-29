import msgpack
import hmac
import hashlib
from cryptography.fernet import Fernet
from AEClient import AEClient

class AEADClient(AEClient):
    def encrypt_message(self, message: str) -> dict:
        """Ajoute un HMAC pour garantir l'intégrité."""
        encrypted = super().encrypt_message(message)
        hmac_digest = hmac.new(self.fernet.key, encrypted, hashlib.sha256).digest()
        return {"enc_msg": encrypted, "hmac": hmac_digest}

    def decrypt_message(self, frame: dict) -> str:
        """Vérifie l'intégrité avant de déchiffrer."""
        if hmac.new(self.fernet.key, frame["enc_msg"], hashlib.sha256).digest() != frame["hmac"]:
            raise Exception("Message modifié !")
        return super().decrypt_message(frame["enc_msg"])
