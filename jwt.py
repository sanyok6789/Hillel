import jwt
import time
from datetime import datetime, timedelta

# Секретний ключ для підпису токену. Потрібно зберегти його у секреті.
SECRET_KEY = '...'

def encode_token(payload):
    # Параметри токену
    payload['iat'] = datetime.utcnow()  # Час видачі токену
    payload['exp'] = datetime.utcnow() + timedelta(minutes=15)  # Час життя токену: 15 хвилин

    # Кодування та підпис токену
    encoded_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return encoded_token

def decode_token(token):
    try:
        decoded_payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        raise ValueError('Expired token')
    except jwt.DecodeError:
        raise ValueError('Invalid token')

# Приклад використання:
if __name__ == "__main__":
    user_data = {
        'username': 'john_doe',
        'role': 'user'
    }

    # Кодування та вивід токену
    encoded_token = encode_token(user_data)
    print("Encoded Token:", encoded_token)

    # Спроба декодування токену
    try:
        decoded_payload = decode_token(encoded_token)
        print("Decoded Payload:", decoded_payload)
    except ValueError as e:
        print("Error:", e)