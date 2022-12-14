from cryptography.fernet import Fernet


def check_user_password(username, password):
    """
    checks is the user inputted a valid username and password to register
    for the password manager
    :param username: the user inputted username
    :param password: the user inputted password
    :return: a bool value if both username and password are valid entries
    """
    user = list(username)  # turn username into a list of its chars
    for char in user:
        # check for every char if it is a space, if so, return False
        if char == " ":
            print("Username Cannot Have Spaces")
            return False
    pass_list = list(password)  # turn password into a list of chars
    has_caps = False
    has_digit = False
    has_space = False
    length = 0
    for char in pass_list:
        # if the char is an uppercase letter, set has_caps to True
        if char.isupper():
            has_caps = True
        # if char is a number, set has_digit to True
        elif char.isnumeric():
            has_digit = True
        # if char is a space, set has_space to True (makes sure it does not pass)
        elif char == " ":
            has_space = True
        length += 1  # increment length
    # check if has_caps and has_digit is True, has_space is False, and length
    # of password is at least 8 chars, if all conditions are met, return True
    if (has_caps is True and has_space is False and has_digit is True
            and length >= 8):
        return True
    # if a condition fails, print why password failed and return False
    if has_caps is False:
        print("Password Must Have One Upper Case Letter")
    if has_space is True:
        print("Password Cannot Have Spaces")
    if has_digit is False:
        print("Password Must Have One Digit")
    return False


def registration(username, password):
    """
    checks if the user credentials are valid, if so, register user and add
    login information into txt files
    :param username: the user inputted username
    :param password: the user inputted password
    :return: only returns False if check_user_password returns False as well
    """
    # check username and password, if either is not valid, return False
    if check_user_password(username, password) is False:
        print("Invalid Credentials")
        return False
    # if registration is successful and both credentials pass
    else:
        # generate a unique key for the user's registration
        key = Fernet.generate_key()
        f = Fernet(key)
        # open database.txt
        file = open("database.txt", 'a')
        # convert password to bytes and encrypt using the key
        byte_pass = bytes(password, 'utf-8')
        encrypt_pass = f.encrypt(byte_pass)
        # write to txt the username and password
        file.write(str(username) + '\t')
        file.write(str(encrypt_pass))
        file.write('\n')
        file.close()
        # open keys to hold the login's key and write the key used
        key_file = open("keys.txt", 'a')
        key_file.write(str(key))
        key_file.write('\n')
        key_file.close()


def main():
    """
    Standalone execution of register.py

    """
    username = input("Enter a username to check: ")
    password = input("Enter a password to check: ")
    print(check_user_password(username, password))


if __name__ == "__main__":
    main()
