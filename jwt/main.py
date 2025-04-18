import secrets
import jwt 
from datetime import datetime, timedelta


secret_key = secrets.token_urlsafe(32)
print("SECRET_KEY:", secret_key)

def create_jwt(user_id: str) -> str:
    payload = {
        "sub": user_id,
        "exp": datetime.now() + timedelta(minutes=30)
    }
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token

user_id = "sad"
token = create_jwt(user_id)
print(f"JWT_TOKEN: {token}")