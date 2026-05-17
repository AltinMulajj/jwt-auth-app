import socket
import json
import getpass
from commands import send_command

HOST = "localhost"
PORT = 8080

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    credentials = json.dumps({"username": username, "password": password})
    sock.send(credentials.encode())

    response = sock.recv(1024).decode()

    if response.startswith("ERROR"):
        print("Login failed:", response)
        sock.close()
        return

    token = response
    print(f"Logged in. JWT token is: {token}")

    while True:
        command = input("Enter command ('request_data' or 'logout'): ").strip()

        if command == "request_data":
            result = send_command(sock, "request_data", token)
            print("Protected data received:", result)

        elif command == "logout":
            result = send_command(sock, "logout", token)
            print(result)
            print("Logging out...")
            break

        else:
            print("Unknown command.")

    sock.close()

if __name__ == "__main__":
    main()