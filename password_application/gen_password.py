import string
import tkinter as tk
import random
from tkinter import messagebox
from tkinter.simpledialog import askinteger


def generate(num_letters, num_numbs, num_spec):
    """
    Generate a password with a set number of letters, numbers, and
    special characters designated by the user
    :param num_letters: the number of letters the user wants
    :param num_numbs: the number of numbers the user wants
    :param num_spec: the number of special characters the user wants
    :return: a password or None if the total length of the password desired
    is 0 or above 30
    """
    # get total length of desired password
    total_chars = num_letters + num_numbs + num_spec
    # is the total length is 0 or above 30, show warning to user
    if total_chars > 30 or total_chars == 0:
        tk.messagebox.showwarning("INVALID", "Invalid number of letters, "
                                             "numbers, and special characters \n"
                                             "Max Characters : 30. "
                                             "Min Characters: 1")
    # user inputted an acceptable desired password length
    else:
        # list to hold all chars for password
        password = []
        # all possible letters for the password
        poss_letters = string.ascii_letters
        # all possible numbers for the password
        poss_nums = string.digits
        # all possible special characters for the password
        poss_special = string.punctuation
        # counter for all types of chars possible
        letter_counter = 0
        num_counter = 0
        spec_counter = 0
        # while the length of password list is less than the desired length
        while len(password) < total_chars:
            # get random int choice to decide type of  char
            # 1: letter
            # 2: number
            # 3: special character
            choice = random.randint(1, 3)
            # if choice is 1 and the letter_counter is less than desired number
            # of letters, append random letter to list
            if choice == 1 and letter_counter < num_letters:
                password.append(random.choice(poss_letters))
            # if choice is 2 and the num_counter is less than desired number
            # of numbers, append random number to list
            elif choice == 2 and num_counter < num_numbs:
                password.append(random.choice(poss_nums))
            # if choice is 3 and the spec_counter is less than desired number
            # of special chars, append random special char to list
            elif choice == 3 and spec_counter < num_spec:
                password.append(random.choice(poss_special))
        # turn list to string with no spaces and return it
        return "".join(password)


def main():
    """
    ask the user for the number of letters, numbers, and special chars
    for the new password and call generate to create the password
    :return: "None" is the user cancels a dislog box or the
    string converted password from generate (to handle is None is returned)
    """
    pass_chars = askinteger("New Password",
                            "Enter the number of letters for new "
                            "password between 0-30: ", minvalue=0,
                            maxvalue=30)
    if pass_chars is None:
        return "None"

    pass_numbs = askinteger("New Password",
                            "Enter the number of numbers for new "
                            "password between 0-30: ", minvalue=0,
                            maxvalue=30)
    if pass_numbs is None:
        return "None"

    pass_spec = askinteger("New Password",
                           "Enter the number of special characters for new "
                           "password between 0-30: ", minvalue=0,
                           maxvalue=30)
    if pass_spec is None:
        return "None"

    password = generate(pass_chars, pass_numbs, pass_spec)
    return str(password)


if __name__ == "__main__":
    main()
