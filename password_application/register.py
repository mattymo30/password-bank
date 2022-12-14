from cryptography.fernet import Fernet


def registration(username, password):
    key = Fernet.generate_key()
    f = Fernet(key)
    file = open("database.txt", 'a')
    byte_pass = bytes(password, 'utf-8')
    encrypt_pass = f.encrypt(byte_pass)
    file.write(str(username) + '\t')
    file.write(str(encrypt_pass))
    file.write('\n')
    file.close()
    key_file = open("keys.txt", 'a')
    key_file.write(str(key))
    key_file.write('\n')
    key_file.close()
