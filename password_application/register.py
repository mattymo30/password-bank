from cryptography.fernet import Fernet


def check_user_password(username, password):
    user = list(username)
    for char in user:
        if char == " ":
            print("Username Cannot Have Spaces")
            return False
    pass_list = list(password)
    has_caps = False
    has_digit = False
    has_space = False
    length = 0
    for char in pass_list:
        if char.isupper():
            has_caps = True
        elif char.isnumeric():
            has_digit = True
        elif char == " ":
            has_space = True
        length += 1
    if has_caps is True and has_space is False and has_digit is True and length >= 8:
        return True
    if has_caps is False:
        print("Password Must Have One Upper Case Letter")
    if has_space is True:
        print("Password Cannot Have Spaces")
    if has_digit is False:
        print("Password Must Have One Digit")
    return False


def registration(username, password):
    if check_user_password(username, password) is False:
        print("Invalid Credentials")
        return False
    else:
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


def main():
    username = input("Enter a username to check: ")
    password = input("Enter a password to check: ")
    print(check_user_password(username, password))


if __name__ == "__main__":
    main()