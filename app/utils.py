import bcrypt


def hash_password(password: str) -> str:
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password.decode()


def verify_password(plain_password: str, hashed_password: str) -> bool:
    valid = bcrypt.checkpw(plain_password.encode(), hashed_password.encode())
    return valid
