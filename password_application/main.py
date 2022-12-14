from tkinter import *  # import tkinter for GUI
import register

# start up a screen with dimensions of 400x300 pixels
login_screen = Tk()
login_screen.title("Login Page")
width = 400
height = 300
screen_width = login_screen.winfo_screenwidth()  # Width of the screen
screen_height = login_screen.winfo_screenheight()  # Height of the screen
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
login_screen.geometry("%dx%d+%d+%d" % (width, height, x, y))


def change_to_login():
    """
    change screen to the login frame from either entry or register
    frame
    """
    # change title of screen
    login_screen.title("Login")
    # clear screen of any widgets so widgets associated with login_frame show
    register_frame.forget()
    entry_frame.forget()
    # pack screen with all login_frame widgets
    login_frame.pack(fill='both', expand=1)


def change_to_register():
    """
    change screen to the register frame from either entry or login
    frame
    """
    # change title of screen
    login_screen.title("Register User")
    # clear screen of any widgets so widgets associated with
    # register_frame show
    login_frame.forget()
    entry_frame.forget()
    # pack screen with all register_frame widgets
    register_frame.pack(fill='both', expand=1)


def change_to_entry():
    """
    change screen to the entry frame from either register or login
    frame
    """
    # change title of screen
    login_screen.title("Login Page")
    # clear screen of any widgets so widgets associated with
    # entry_frame show
    login_frame.forget()
    register_frame.forget()
    # pack screen with all entry_frame widgets
    entry_frame.pack(fill='both', expand=1)


def check_register(user, passw):
    did_register = register.registration(user, passw)
    if did_register is False:
        is_good_register.config(text="Please enter a valid username and"
                                     " password", fg="Red")
    else:
        is_good_register.config(text="Registration Successful", fg="Green")


def login(user, passw):
    login_correct = register.check_login(user, passw)
    if login_correct is True:
        login_success.config(text="Login Successful", fg="Green")
    else:
        login_success.config(text="Login failed. Please check username and"
                                  " password", fg="Red")


# create all frames, only one will be visible at a time
login_frame = Frame(login_screen)
register_frame = Frame(login_screen)
entry_frame = Frame(login_screen)

# widgets for entry_frame
Label(entry_frame, text="Password Bank", font=25).pack()
Label(entry_frame, text="").pack()
Button(entry_frame, text="Login", height="2", width="30", command=change_to_login).pack()
Label(entry_frame, text="").pack()
Button(entry_frame, text="Register", height="2", width="30", command=change_to_register).pack()

# widgets for register frame
Label(register_frame, text="Register User", font=25).pack()
Label(register_frame, text="First Name").pack()

Label(register_frame, text="Username").pack()
username = Entry(register_frame)
username.pack()
Label(register_frame, text="Password").pack()
password = Entry(register_frame)
password.pack()
Button(register_frame, text="Register", height='2', width='20',
       command=lambda: check_register(username.get(), password.get())).pack()
Button(register_frame, text="Back", height='2', width='20', command=change_to_entry).pack()
is_good_register = Label(register_frame, text="")
is_good_register.pack()


# widgets for login frame
Label(login_frame, text="Login", font=25).pack()
Label(login_frame, text="Username").pack()
login_username = Entry(login_frame)
login_username.pack()
Label(login_frame, text="Password").pack()
login_password = Entry(login_frame, show='*')
login_password.pack()
Button(login_frame, text="Login", height='2', width='20', command=lambda: login(login_username.get(), login_password.get())).pack()
Button(login_frame, text="Back", height='2', width='20', command=change_to_entry).pack()
login_success = Label(login_frame, text="")
login_success.pack()

# the entry frame needs to be shown when the program starts
# pack to screen first and call mainloop() on the login_screen
entry_frame.pack(fill='both', expand=1)
login_screen.mainloop()
