```markdown
# JWT Authentication Console Application

## Description
Client-server console application with JWT authentication using RSA 2048-bit asymmetric keys.

## Requirements
- Python 3.12
- OpenSSL

## Installation
```bash
python3 -m pip install PyJWT cryptography --break-system-packages
```

## Generate RSA Keys
```bash
mkdir keys
openssl genrsa -out keys/private_key.pem 2048
openssl rsa -in keys/private_key.pem -pubout -out keys/public_key.pem
```

## How to Run

**Terminal 1 — Server:**
```bash
cd jwt-auth-app
python3 server/server.py
```

**Terminal 2 — Client:**
```bash
cd jwt-auth-app
python3 client/client.py
```

## Commands
| Command | Description |
|---------|-------------|
| `request_data` | Access protected data |
| `logout` | End session and discard token |

## Test Credentials
| Username | Password |
|----------|----------|
| jane_doe | password123 |
| john_doe | secret456 |

## Project Structure
```
jwt-auth-app/
├── server/
│   ├── server.py
│   ├── auth.py
│   └── jwt_handler.py
├── client/
│   ├── client.py
│   └── commands.py
├── keys/
│   ├── private_key.pem
│   └── public_key.pem
├── requirements.txt
└── README.md
```

## Note
- Make sure the server is running before starting the client
- Token expires after 1 hour — login again to get a new one
```
