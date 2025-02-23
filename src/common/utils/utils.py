import secrets
import string
from datetime import datetime


def generate_random_key(length=32) -> str:
    characters = string.ascii_letters + string.digits
    return "".join(secrets.choice(characters) for _ in range(length))


def datetime_now() -> int:
    return int(datetime.now().timestamp())
