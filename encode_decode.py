
import json
import base64
import time
import hashlib


def encode(payload, secret):
    payload["exp"] = time.time() + 15 * 60  # Установить срок действия токена на 15 минут
    payload["iat"] = time.time()  # Время видачі токена

    # Кодирование payload
    payload_encoded = base64.b64encode(json.dumps(payload).encode())

    # Подпись
    signature = base64.b64encode(hashlib.sha256((payload_encoded + secret.encode()).strip()).digest())

    # Формирование токена
    token = payload_encoded + b"." + signature

    return token


def decode(token, secret):
    payload_encoded, signature = token.split(b".")

    # Проверка подписи
    signature_check = base64.b64encode(hashlib.sha256((payload_encoded + secret.encode()).strip()).digest())
    if signature != signature_check:
        raise Exception("Invalid token signature")

    payload_json = base64.b64decode(payload_encoded)
    payload = json.loads(payload_json)

    # Проверка срока действия токена
    if time.time() > payload["exp"]:
        raise Exception("Token has expired")

    return payload
