import tkinter as tk
import random
from tkinter import messagebox
WINDOW = tk.Tk()
WINDOW.geometry("400x400")
new_pass = tk.StringVar()


def generate(pass_length):
    password = ""
    poss_symbol = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                   'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                   '!', '#', '$', '%', '&', '(', ')', '*', '+']
    for n in range(pass_length):
        password = password + random.choice(poss_symbol)

    return password


def get_pass_len():
    user_length = int(password_len.get())
    if user_length <= 0 or user_length > 30:
        tk.messagebox.showinfo("INVALID", "Invalid number of digits")
    else:
        new_password.config(text=generate(user_length))


password_label = tk.Label(WINDOW, text="Enter the number of digits for new password between"
                                       " 1-30: ")
password_label.pack()
password_len = tk.Entry(WINDOW)
password_len.pack()
new_password = tk.Label(WINDOW, text="New Password")
new_password.pack()
find_len = tk.Button(WINDOW, text="Get Password", command=get_pass_len)
find_len.pack()
WINDOW.mainloop()
"""
password_length = int(input("Enter the number of digits for new password between"
                            " 1-30: "))
if password_length <= 0 or password_length > 30:
    print("INVALID NUMBER OF DIGITS")
else:
    print(generate(password_length))
"""
