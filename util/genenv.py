import os
import binascii
import sys

if __name__ == '__main__':
    secret_key = binascii.hexlify(os.urandom(24)).decode()
    print("SECRET_KEY={0}".format(secret_key))
