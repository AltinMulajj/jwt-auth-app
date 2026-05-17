import socket
import json
from auth import validate_credentials
from jwt_handler import generate_token, verify_token

HOST = "localhost"
PORT = 8080

def handle_client(conn):
    print("Connection established.")
    print("Awaiting credentials...")

    data = conn.recv(1024).decode()
    credentials = json.loads(data)
    username = credentials.get("username")
    password = credentials.get("password")

    if validate_credentials(username, password):
        print("Authentication successful. JWT issued.")
        token = generate_token(username)
        conn.send(token.encode())
    else:
        print("Authentication failed.")
        conn.send(b"ERROR: Invalid credentials")
        conn.close()
        return

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break

        request = json.loads(data)
        command = request.get("command")
        token = request.get("token")

        payload = verify_token(token)

        if command == "request_data":
            if payload:
                response = json.dumps({"data": "This is protected data."})
                conn.send(response.encode())
            else:
                conn.send(b"401 Unauthorized")

        elif command == "logout":
            print("Client logged out.")
            conn.send(b"Logged out successfully.")
            break

    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(1)
    print("Waiting for connections...")

    while True:
        conn, addr = server.accept()
        handle_client(conn)

if __name__ == "__main__":
    start_server()