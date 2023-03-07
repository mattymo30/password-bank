import tkinter as tk
import random
from tkinter import messagebox
from tkinter.simpledialog import askinteger


def generate(digits):
    if digits <= 0 or digits > 30:
        tk.messagebox.showwarning("INVALID", "Invalid number of digits")
    else:
        password = ""
        poss_symbol = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't',
                       'u',
                       'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                       'O',
                       'P',
                       'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                       '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                       '!', '#', '$', '%', '&', '(', ')', '*', '+']
        for n in range(digits):
            password = password + random.choice(poss_symbol)

        return password


def main():
    password_digits = \
        askinteger("New Password",
                   "Enter the number of digits for new "
                   "password between 1-30: ")
    password = generate(password_digits)
    return str(password)


if __name__ == "__main__":
    main()
