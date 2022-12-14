from cryptography.fernet import Fernet


key = Fernet.generate_key()
f = Fernet(key)


def registration(username, password):
    file = open("database.txt", 'wt')
    byte_pass = bytes(password, 'utf-8')
    encrypt_pass = f.encrypt(byte_pass)
    file.write(str(username))
    file.write(str(encrypt_pass))
    file.close()
