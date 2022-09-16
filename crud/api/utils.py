import hashlib


def make_hash_with_salt(salt: str, password: str) -> str:
    encoded_string = (salt + password).encode("utf-8")
    hash = hashlib.sha256(encoded_string).hexdigest()
    return hash