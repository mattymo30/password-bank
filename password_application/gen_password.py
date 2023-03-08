import string
import tkinter as tk
import random
from tkinter import messagebox
from tkinter.simpledialog import askinteger


def generate(num_letters, num_numbs, num_spec):
    total_chars = num_letters + num_numbs + num_spec
    if total_chars > 30 or total_chars <= 0:
        tk.messagebox.showwarning("INVALID", "Invalid number of letters, "
                                             "numbers, and special characters")
    else:
        password = []
        poss_letters = string.ascii_letters
        poss_nums = string.digits
        poss_special = string.punctuation

        letter_counter = 0
        num_counter = 0
        spec_counter = 0
        while len(password) < total_chars:
            choice = random.randint(1, 3)
            if choice == 1 and letter_counter < num_letters:
                password.append(random.choice(poss_letters))
            elif choice == 2 and num_counter < num_numbs:
                password.append(random.choice(poss_nums))
            elif choice == 3 and spec_counter < num_spec:
                password.append(random.choice(poss_special))

        return "".join(password)


def main():
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
