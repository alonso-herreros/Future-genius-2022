from os import listdir
from os.path import dirname, join
import hashlib


def hash(password):
    password = password.encode()
    result = hashlib.sha1(password)
    hashedPassword = result.hexdigest()
    return hashedPassword


def find_password(hashed):
    rockyou_dir = join(dirname(__file__), "rockyou")
    for file in listdir(rockyou_dir):
        with open(join(rockyou_dir, file), "r", errors="ignore") as rockyou:
            passwords = rockyou.read().split("\n")
            for password in passwords:
                if hash(password) == hashed: return password
    return "No password was found to match the hash"


stolenPassword_hashed = "d77bd8482003072cc056575c0478476a3af1993c"

if __name__ == "__main__":
    print("got:", find_password(input("hash: ") or stolenPassword_hashed))