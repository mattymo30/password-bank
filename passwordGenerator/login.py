from tkinter import *


def main_screen_login():
    login_screen = Tk()
    login_screen.title("Login Page")
    login_screen.geometry("400x300")
    Label(text="Password Bank", font=25).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30").pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
    login_screen.mainloop()


def register():
    register_screen = Tk()
    register_screen.title("Registration")
    register_screen.geometry("400x300")
    Label(register_screen, text="Username").pack()
    Entry(register_screen).pack()
    Label(register_screen, text="Password").pack()
    Entry(register_screen).pack()
    register_screen.mainloop()


def main():
    main_screen_login()


if __name__ == "__main__":
    main()
