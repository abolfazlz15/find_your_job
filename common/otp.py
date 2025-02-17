import random

from django.core.cache import cache


def get_otp(key: str):
    return cache.get(f"otp:{key}")

def generate_otp() -> int:
    return random.randint(1000, 9999)

def set_otp(key: str) -> int:
    otp = generate_otp()
    cache.set(f"otp:{key}", otp, timeout=120)
    return otp

def is_otp_valid(key: str, code: str) -> bool:
    try:
        otp = get_otp(key=key)

        return str(otp) == str(code)
    except (ValueError, KeyError):
        return False