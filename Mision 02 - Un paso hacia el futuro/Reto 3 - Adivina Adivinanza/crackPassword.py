import hashlib


def hash(password):
    password = password.encode()
    result = hashlib.sha1(password)
    hashedPassword = result.hexdigest()
    return hashedPassword


stolenPassword_hashed = "d77bd8482003072cc056575c0478476a3af1993c"
