import requests
from pydantic import BaseModel

api_key = "2281337"


class User(BaseModel):
    username: str
    password: str


user_data = User(username="sad", password="123")
url = f"http://127.0.0.1:8080/login/{api_key}/{user_data.username}/{user_data.password}"

response = requests.post(url)
token = response.json()
print(f"TOKEN: {token}\nusername: {user_data.username}")
