from tkinter import *  # import tkinter for GUI
from tkinter import messagebox
import register  # for registration and log


# start up a screen with dimensions of 400x300 pixels
login_screen = Tk()
login_screen.title("Login Page")
width = 500
height = 400
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
    """
    check that the user successfully registered with the correct credentials
    using register's registration function
    :param user: the user given username for registration
    :param passw: the user given password for registration
    """
    # check if there are any errors and if the registration was successful
    error_list, did_register = register.registration(user, passw)
    # if registration failed
    if did_register is False:
        # concatenate a string of all the errors in error_list and output
        # to user
        error_message = ""
        for error in error_list:
            error_message += error + "\n"
        messagebox.showerror(title="Registration Unsuccessful",
                             message=error_message)
    # if registration was successful output to user and reset frame to
    # empty fields
    else:
        is_good_register.config(text="Registration Successful", fg="Green")
        username.delete(0, END)
        password.delete(0, END)


def login(user, passw):
    """
    check if a user login was successful using register's check_login function
    :param user: the user given username
    :param passw:  the user given password
    """
    # check if login was successful and if there were any errors
    error, login_correct = register.check_login(user, passw)
    # if login was a success
    if login_correct is True:
        # destroy the login screen and call password_manager to access the
        # user's specific password manager
        login_screen.destroy()
        import password_manager
        password_manager.main(user)
    # if login failed, output the error that caused the fail to the user
    else:
        login_success.config(text="Login failed. " + error, fg="Red")


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


def main():
    login_screen.mainloop()


if __name__ == "__main__":
    main()
