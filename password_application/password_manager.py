from tkinter import *
import sqlite3

# start up screen with dimensions 400x300 centered to user's screen
manager_screen = Tk()
manager_screen.title("Password Manager")
width = 500
height = 400
screen_width = manager_screen.winfo_screenwidth()  # Width of the screen
screen_height = manager_screen.winfo_screenheight()  # Height of the screen
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
manager_screen.geometry("%dx%d+%d+%d" % (width, height, x, y))


def config_table(username):
    """
    initial configuration of database for user when user logs in
    :param username: the user's given username
    :return: the connection to the sqlite3 database specified for the user
    """
    conn = sqlite3.connect(username + ".db")
    cursor = conn.cursor()
    cursor.execute("""
                    CREATE TABLE IF NOT EXISTS manager (
                    website NOT NULL, 
                    url NOT NULL, 
                    id NOT NULL, 
                    password NOT NULL)""")
    return conn


def open_table(username):
    """
    open database for user without attempting to create a table
    each time
    :param username: the user given username
    :return: the connection and cursor to the user's database
    """
    conn = sqlite3.connect(username + ".db")
    cursor = conn.cursor()
    return conn, cursor


def submit_new():
    """
    submit a new set of information into the user's database
    """
    # open the table in the user's database
    conn, cursor = open_table(user_login)
    # check that all entries from the user are not empty
    if (web_name.get() != "" and url_name.get() != ""
            and user_id.get() != "" and password.get() != ""):
        # execute cursor to insert the values into the database
        cursor.execute("INSERT INTO manager "
                       "VALUES (:website, :url, :id, :password)",
                       {
                           'website': web_name.get(),
                           'url': url_name.get(),
                           'id': user_id.get(),
                           'password': password.get()
                       }
                       )
        conn.commit()
        conn.close()
        web_name.delete(0, END)
        url_name.delete(0, END)
        user_id.delete(0, END)
        password.delete(0, END)
        did_add.config(text="Successfully Submitted!", fg="Green")
    # if a entry field is left blank
    else:
        did_add.config(text="Submission Unsuccessful. "
                            "No Entry Can Be Blank", fg="Red")


def display():
    """
    display all entries from the user
    """
    # open table in user's database
    conn, cursor = open_table(user_login)
    cursor.execute("SELECT *, oid FROM manager")
    # fetch all records in the database and set a string to hold all vals
    records = cursor.fetchall()
    site_display.delete("1.0", "end")
    url_display.delete("1.0", "end")
    user_display.delete("1.0", "end")
    pass_display.delete("1.0", "end")
    all_sites = "Site:\n"
    all_url = "URL:\n"
    all_users = "ID:\n"
    all_pass = "Password:\n"
    for record in records:
        all_sites += record[0] + "\n"
        all_url += record[1] + "\n"
        all_users += record[2] + "\n"
        all_pass += record[3] + "\n"
    site_display.insert(INSERT, all_sites)
    site_display.grid(row=1, column=0)
    url_display.insert(INSERT, all_url)
    url_display.grid(row=1, column=1)
    user_display.insert(INSERT, all_users)
    user_display.grid(row=1, column=2)
    pass_display.insert(INSERT, all_pass)
    pass_display.grid(row=1, column=3)
    conn.commit()
    conn.close()
    """
    all_recs = "Site:\tURL:\tID:\tPassword:\n"
    for record in records:
        all_recs += record[0] + "\t" + record[1] + "\t" + record[2] + \
                    "\t" + record[3] + "\n"
    query_display.insert(INSERT, all_recs)
    query_display.pack()
    conn.commit()
    conn.close()
    """


def update():
    """
    update an existing entry in the user's database
    """
    # check if user did not leave the site entry as blank
    if site_app.get() != "":
        # check if new username and new password entries are not blank
        if new_user_id.get() != "" or new_pass.get() != "":
            conn, cursor = open_table(user_login)
            cursor.execute("SELECT *, oid FROM manager")
            records = cursor.fetchall()
            for record in records:
                if record[0] == site_app.get():
                    cursor.execute("UPDATE manager SET id=?, "
                                   "password=? WHERE website=?",
                                   (new_user_id.get(), new_pass.get(),
                                    site_app.get()))
                    conn.commit()
                    conn.close()
                    update_success.config(text="Update Successful", fg="Green")
                    site_app.delete(0, END)
                    new_user_id.delete(0, END)
                    new_pass.delete(0, END)
                    return
            update_success.config(text="Update Unsuccessful. Site/App "
                                       "Does Not Exist in Database", fg="Red")
        else:
            update_success.config(text="Update Unsuccessful. New Username or "
                                       "Password Cannot Be Blank", fg="Red")
    else:
        update_success.config(text="Update Unsuccessful. Site/App "
                                   "Cannot Be Blank", fg="Red")


def delete_info():
    """
    delete an entry in the user's database
    """
    # check if site entry was not left blank by user
    if delete_site.get() != "":
        conn, cursor = open_table(user_login)
        cursor.execute("SELECT *, oid FROM manager")
        records = cursor.fetchall()
        for record in records:
            if record[0] == delete_site.get():
                cursor.execute("DELETE FROM manager WHERE website=?",
                               (delete_site.get(),))
                conn.commit()
                conn.close()
                delete_success.config(text="Deletion Successful", fg="Green")
                delete_site.delete(0, END)
                return
        delete_success.config(text="Deletion Unsuccessful. Site/App "
                                   "Does Not Exist in Database", fg="Red")
    else:
        delete_success.config(text="Deletion Unsuccessful. Site/App "
                                   "Cannot Be Blank", fg="Red")


def change_to_add():
    """
    change frame to the add frame
    """
    manager_screen.title("Add New Query")
    main_menu.forget()
    update_frame.forget()
    query_frame.forget()
    add_frame.pack(fill="both", expand=1)
    did_add['text'] = ""


def change_to_update():
    """
    change frame to the update frame
    """
    manager_screen.title("Update Query")
    main_menu.forget()
    add_frame.forget()
    query_frame.forget()
    delete_frame.forget()
    update_frame.pack(fill="both", expand=1)
    update_success['text'] = ""


def change_to_query():
    """
    change frame to the query frame
    """
    manager_screen.title("Show Info")
    main_menu.forget()
    add_frame.forget()
    update_frame.forget()
    delete_frame.forget()
    query_frame.pack(fill="both", expand=1)
    site_display.delete("1.0", "end")
    url_display.delete("1.0", "end")
    user_display.delete("1.0", "end")
    pass_display.delete("1.0", "end")


def change_to_main():
    """
    change frame to the main frame
    """
    manager_screen.title("Password Manager")
    query_frame.forget()
    add_frame.forget()
    update_frame.forget()
    delete_frame.forget()
    main_menu.pack(fill="both", expand=1)


def change_to_delete():
    """
    change frame to the delete frame
    """
    manager_screen.title("Delete Entry")
    query_frame.forget()
    add_frame.forget()
    update_frame.forget()
    main_menu.forget()
    delete_frame.pack(fill="both", expand=1)
    delete_success['text'] = ""


# create all the frames for the manager
main_menu = Frame(manager_screen)
add_frame = Frame(manager_screen)
update_frame = Frame(manager_screen)
query_frame = Frame(manager_screen)
delete_frame = Frame(manager_screen)

# main frame widgets
Label(main_menu, text="Welcome!", font=25).pack()
Label(main_menu, text="").pack()
Button(main_menu, text="Add New Record", height="2", width="30",
       command=change_to_add).pack()
Label(main_menu, text="").pack()
Button(main_menu, text="Update Record", height="2", width="30",
       command=change_to_update).pack()
Label(main_menu, text="").pack()
Button(main_menu, text="Delete Entries", height="2", width="30",
       command=change_to_delete).pack()
Label(main_menu, text="").pack()
Button(main_menu, text="Show All Records", height="2", width="30",
       command=change_to_query).pack()

# add frame widgets
Label(add_frame, text="Add New Record", font=25).pack()
Label(add_frame, text="Website/App").pack()
web_name = Entry(add_frame)
web_name.pack()
Label(add_frame, text="URL").pack()
url_name = Entry(add_frame)
url_name.pack()
Label(add_frame, text="Username/ID").pack()
user_id = Entry(add_frame)
user_id.pack()
Label(add_frame, text="Password").pack()
password = Entry(add_frame)
password.pack()
Button(add_frame, text="Add",
       command=submit_new).pack()
Button(add_frame, text="Back To Main",
       command=change_to_main).pack()
did_add = Label(add_frame, text="")
did_add.pack()


# update frame widgets
Label(update_frame, text="Update Record", font=25).pack()
Label(update_frame, text="Website/App to Update").pack()
site_app = Entry(update_frame)
site_app.pack()
Label(update_frame, text="New Username/ID").pack()
new_user_id = Entry(update_frame)
new_user_id.pack()
Label(update_frame, text="New Password").pack()
new_pass = Entry(update_frame)
new_pass.pack()
Button(update_frame, text="Update", command=update).pack()
Button(update_frame, text="Back To Main", command=change_to_main).pack()
update_success = Label(update_frame, text="")
update_success.pack()


# query frame widgets (grid format)
Label(query_frame, text="All Records", font=25, justify=CENTER).grid(row=0,
                                                                     column=1,
                                                                     columnspan=2)
site_display = Text(query_frame, width=15, height=20)
site_display.grid(row=1, column=0)
url_display = Text(query_frame, width=15, height=20)
url_display.grid(row=1, column=1)
user_display = Text(query_frame, width=15, height=20)
user_display.grid(row=1, column=2)
pass_display = Text(query_frame, width=15, height=20)
pass_display.grid(row=1, column=3)
Label(query_frame, text="").grid(row=2)
Button(query_frame, text="Back To Main", anchor="s", command=change_to_main)\
    .grid(row=3, column=2)
show_query = Button(query_frame, text="Show Saved Info", command=display)
show_query.grid(row=3, column=1)


# query frame widgets (pack format)
"""
Label(query_frame, text="All Records", font=25).pack()
query_display = Text(query_frame)
query_display.pack()
Button(query_frame, text="Back To Main", anchor="s", command=change_to_main).pack(side="bottom")
show_query = Button(query_frame, text="Show All Saved Info", command=display)
show_query.pack(side="bottom")
v = Scrollbar(query_frame, orient='vertical')
v.pack(side=RIGHT, fill=Y)
v.config(command=query_display.yview)
"""


# delete frame widgets
Label(delete_frame, text="Delete Entry").pack()
Label(delete_frame, text="Entry to be Deleted:").pack()
delete_site = Entry(delete_frame)
delete_site.pack()
Button(delete_frame, text="Delete", command=delete_info).pack()
Button(delete_frame, text="Back To Main", command=change_to_main).pack()
delete_success = Label(delete_frame, text="")
delete_success.pack()


# the main frame needs to be shown when the program starts
# pack to screen first and call mainloop() on the manager_screen
main_menu.pack(fill='both', expand=1)


def main(username="passmanager"):
    # holds username from main.py when user logs in
    global user_login
    user_login = username
    # configure a new table if necessary
    user_conn = config_table(user_login)
    user_conn.commit()
    user_conn.close()
    manager_screen.mainloop()


if __name__ == "__main__":
    main()
