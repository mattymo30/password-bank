from tkinter import *  # import tkinter for GUI

# start up a screen with dimensions of 400x300 pixels
login_screen = Tk()
login_screen.title("Login Page")
width = 400
height = 300
screen_width = login_screen.winfo_screenwidth()  # Width of the screen
screen_height = login_screen.winfo_screenheight()  # Height of the screen
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
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
Entry(register_frame).pack()
Label(register_frame, text="Password").pack()
Entry(register_frame).pack()
Button(register_frame, text="Register", height='2', width='20').pack()
Button(register_frame, text="Back", height='2', width='20', command=change_to_entry).pack()


# widgets for login frame
Label(login_frame, text="Login", font=25).pack()
Label(login_frame, text="Username").pack()
Entry(login_frame).pack()
Label(login_frame, text="Password").pack()
Entry(login_frame, show='*').pack()
Button(login_frame, text="Login", height='2', width='20').pack()
Button(login_frame, text="Back", height='2', width='20', command=change_to_entry).pack()

# the entry frame needs to be shown when the program starts
# pack to screen first and call mainloop() on the login_screen
entry_frame.pack(fill='both', expand=1)
login_screen.mainloop()
