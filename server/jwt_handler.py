import jwt
from datetime import datetime, timedelta

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, "keys/private_key.pem"), "r") as f:
    PRIVATE_KEY = f.read()

with open(os.path.join(BASE_DIR, "keys/public_key.pem"), "r") as f:
    PUBLIC_KEY = f.read()

def generate_token(username):
    payload = {
        "sub": username,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, PRIVATE_KEY, algorithm="RS256")

def verify_token(token):
    try:
        payload = jwt.decode(token, PUBLIC_KEY, algorithms=["RS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None