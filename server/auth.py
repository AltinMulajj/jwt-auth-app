USERS = {
    "jane_doe": "password123",
    "john_doe": "secret456"
}

def validate_credentials(username, password):
    return USERS.get(username) == password