from cryptography.fernet import Fernet


def check_user_password(username, password):
    """
    checks is the user inputted a valid username and password to register
    for the password manager
    :param username: the user inputted username
    :param password: the user inputted password
    :return: a bool value if both username and password are valid entries
    """
    error_codes = []
    user = list(username)  # turn username into a list of its chars
    for char in user:
        # check for every char if it is a space, if so, return False
        if char == " ":
            error_codes.append(1)
            return error_codes, False
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
    # check has_caps and has_digit is True, has_space is False, and length
    # of password is at least 8 chars, if all conditions are met, return True
    if (has_caps is True and has_space is False and has_digit is True
            and length >= 8):
        return error_codes, True
    # if a condition fails, print why password failed and return False
    if has_caps is False:
        error_codes.append(2)
    if has_space is True:
        error_codes.append(3)
    if has_digit is False:
        error_codes.append(4)
    if length < 8:
        error_codes.append(5)
    return error_codes, False


def registration(username, password):
    """
    checks if the user credentials are valid, if so, register user and add
    login information into txt files
    :param username: the user inputted username
    :param password: the user inputted password
    :return: returns False if check_user_password returns False as well or
    username is already in the database
    """
    data_file = open("database.bin", 'rb')
    error_message_list = []
    for (i, line) in enumerate(data_file):
        # split line based on tabs and decode the username
        line_split = line.split(bytes('\t', 'utf-8'))
        user = line_split[0].decode()
        if user == username:
            data_file.close()
            error_message_list.append("Username Already Exists in Database")
            return error_message_list, False
    data_file.close()
    # check username and password, if either is not valid, return False
    error_list, is_good = check_user_password(username, password)
    if is_good is False:
        for error in error_list:
            if error == 1:
                error_message_list.append("Username Cannot Have Spaces")
            elif error == 2:
                error_message_list.append("Password Must Have "
                                          "One Upper Case Letter")
            elif error == 3:
                error_message_list.append("Password Cannot Have Spaces")
            elif error == 4:
                error_message_list.append("Password Must Have One Digit")
            elif error == 5:
                error_message_list.append("Password Must Be At Least"
                                          " 8 Characters")
        return error_message_list, False
    # if registration is successful and both credentials pass
    else:
        # generate a unique key for the user's registration
        key = Fernet.generate_key()
        f = Fernet(key)
        # open database.txt
        file = open("database.bin", 'ab')
        # convert password to bytes and encrypt using the key
        user = bytes(username, 'utf-8')
        byte_pass = bytes(password, 'utf-8')
        encrypt_pass = f.encrypt(byte_pass)
        # write to txt the username and password
        file.write(user)
        file.write(bytes('\t', 'utf-8'))
        file.write(encrypt_pass)
        file.write(bytes('\n', 'utf-8'))
        file.close()
        # open keys to hold the login's key and write the key used
        key_file = open("keys.bin", 'ab')
        key_file.write(key)
        key_file.write(bytes('\n', 'utf-8'))
        key_file.close()
        return error_message_list, True


def check_login(username, password):
    error_message = ""
    # open binary files that hold login info and keys
    data_file = open("database.bin", 'rb')
    key_file = open("keys.bin", 'rb')
    # for every line in data_file
    for (i, line) in enumerate(data_file):
        # split line based on tabs and decode the username
        line_split = line.split(bytes('\t', 'utf-8'))
        user = line_split[0].decode()
        # if given username matches user
        if user == username:
            # read all lines of key_file and find line where login key should
            # be at
            keys = key_file.readlines()
            user_key = keys[i]
            # decrypt the password from data file and decode into str
            f = Fernet(user_key)
            decrypted_pass = f.decrypt(line_split[1]).decode()
            # if password is correct
            if decrypted_pass == password:
                return error_message, True
            else:
                # password was incorrect
                error_message = "Password is Incorrect"
                return error_message, False
    # if for loop goes through all of data_file and no username matches,
    # return False
    data_file.close()
    key_file.close()
    error_message = "Username not in database"
    return error_message, False


def main():
    """
    Standalone execution of register.py

    """
    username = input("Enter a username to check: ")
    password = input("Enter a password to check: ")
    print(check_user_password(username, password))


if __name__ == "__main__":
    main()
