from tkinter import *

login_screen = Tk()
login_screen.title("Login Page")
login_screen.geometry("400x300")


def change_to_login():
    login_screen.title("Login")
    register_frame.forget()
    entry_frame.forget()
    login_frame.pack(fill='both', expand=1)


def change_to_register():
    login_screen.title("Register User")
    login_frame.forget()
    entry_frame.forget()
    register_frame.pack(fill='both', expand=1)


def change_to_entry():
    login_screen.title("Login Page")
    login_frame.forget()
    register_frame.forget()
    entry_frame.pack(fill='both', expand=1)


login_frame = Frame(login_screen)
register_frame = Frame(login_screen)
entry_frame = Frame(login_screen)


Label(entry_frame, text="Password Bank", font=25).pack()
Label(entry_frame, text="").pack()
Button(entry_frame, text="Login", height="2", width="30", command=change_to_login).pack()
Label(entry_frame, text="").pack()
Button(entry_frame, text="Register", height="2", width="30", command=change_to_register).pack()


Label(register_frame, text="Register User", font=25).pack()
Label(register_frame, text="Username").pack()
Entry(register_frame).pack()
Label(register_frame, text="Password").pack()
Entry(register_frame).pack()
Button(register_frame, text="Register", height='2', width='20').pack()
Button(register_frame, text="Back", height='2', width='20', command=change_to_entry).pack()

Label(login_frame, text="Login", font=25).pack()
Label(login_frame, text="Username").pack()
Entry(login_frame).pack()
Label(login_frame, text="Password").pack()
Entry(login_frame, show='*').pack()
Button(login_frame, text="Login", height='2', width='20').pack()
Button(login_frame, text="Back", height='2', width='20', command=change_to_entry).pack()


entry_frame.pack(fill='both', expand=1)
login_screen.mainloop()
