import socket
import json

def send_command(sock, command, token):
    request = json.dumps({"command": command, "token": token})
    sock.send(request.encode())
    return sock.recv(1024).decode()