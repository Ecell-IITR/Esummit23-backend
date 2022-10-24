
import os
from dotenv import load_dotenv

load_dotenv()

secret = os.getenv('SECRET_KEY')
import jwt

encoded_jwt = jwt.encode({"some": "payload"}, secret, algorithm="HS256")
print(encoded_jwt)
print(jwt.decode(encoded_jwt, secret, algorithms=["HS256"]))