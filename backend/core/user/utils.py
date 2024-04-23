import jwt 
import time
from config import get_settings

def decodeJWT(token:str)->dict:
    decoded_token = jwt.decode(token, f'{get_settings().SECRET_KEY}', algorithms=['HS256'])
    return decoded_token if decoded_token['exp'] >= time.time() else None
    