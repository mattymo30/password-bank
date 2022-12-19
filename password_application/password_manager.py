from tkinter import *
import sqlite3


manager_screen = Tk()
manager_screen.title("Password Manager")
width = 400
height = 300
screen_width = manager_screen.winfo_screenwidth()  # Width of the screen
screen_height = manager_screen.winfo_screenheight()  # Height of the screen
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
manager_screen.geometry("%dx%d+%d+%d" % (width, height, x, y))


def config_table(username):
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
    conn = sqlite3.connect(username + ".db")
    cursor = conn.cursor()
    return conn, cursor


def submit_new():

    conn, cursor = open_table(user_login)
    if (web_name.get() != "" and url_name.get() != ""
            and user_id.get() != "" and password.get() != ""):
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
    else:
        did_add.config(text="Submission Unsuccessful. "
                            "No Entry Can Be Blank", fg="Red")


def display():
    conn, cursor = open_table(user_login)
    cursor.execute("SELECT *, oid FROM manager")
    records = cursor.fetchall()
    all_recs = "Site:\tURL:\tID:\tPassword:\n"
    for record in records:
        all_recs += record[0] + "\t" + record[1] + "\t" + record[2] +\
                    "\t" + record[3] + "\n"
    query_display['text'] = all_recs
    query_display.pack()
    conn.commit()
    conn.close()


def update():
    if site_app.get() != "":
        conn, cursor = open_table(user_login)
        cursor.execute("UPDATE manager SET id=?, password=? WHERE website=?",
                       (new_user_id.get(), new_pass.get(), site_app.get()))
        conn.commit()
        conn.close()
        update_success.config(text="Update Successful", fg="Green")
    else:
        update_success.config(text="Update Unsuccessful. Site/App "
                                   "Cannot Be Blank", fg="Red")


def delete_info():
    if delete_site.get() != "":
        conn, cursor = open_table(user_login)
        cursor.execute("DELETE FROM manager WHERE website=?",
                       (delete_site.get(),))
        conn.commit()
        conn.close()
        delete_success.config(text="Deletion Successful", fg="Green")
    else:
        delete_success.config(text="Deletion Unsuccessful. Site/App "
                                   "Cannot Be Blank", fg="Red")


def change_to_add():
    manager_screen.title("Add New Query")
    main_menu.forget()
    update_frame.forget()
    query_frame.forget()
    add_frame.pack(fill="both", expand=1)


def change_to_update():
    manager_screen.title("Update Query")
    main_menu.forget()
    add_frame.forget()
    query_frame.forget()
    delete_frame.forget()
    update_frame.pack(fill="both", expand=1)


def change_to_query():
    manager_screen.title("Show Info")
    main_menu.forget()
    add_frame.forget()
    update_frame.forget()
    delete_frame.forget()
    query_frame.pack(fill="both", expand=1)
    query_display.pack_forget()


def change_to_main():
    manager_screen.title("Password Manager")
    query_frame.forget()
    add_frame.forget()
    update_frame.forget()
    delete_frame.forget()
    main_menu.pack(fill="both", expand=1)


def change_to_delete():
    manager_screen.title("Delete Entry")
    query_frame.forget()
    add_frame.forget()
    update_frame.forget()
    main_menu.forget()
    delete_frame.pack(fill="both", expand=1)


main_menu = Frame(manager_screen)
add_frame = Frame(manager_screen)
update_frame = Frame(manager_screen)
query_frame = Frame(manager_screen)
delete_frame = Frame(manager_screen)


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

Label(query_frame, text="All Records", font=25).pack()
query_display = Label(query_frame, anchor="nw")
query_display.pack()
show_query = Button(query_frame, text="Show All Saved Info", command=display)
show_query.pack()
Button(query_frame, text="Back To Main", anchor="s", command=change_to_main).pack()


Label(delete_frame, text="Delete Entry").pack()
Label(delete_frame, text="Entry to be Deleted:").pack()
delete_site = Entry(delete_frame)
delete_site.pack()
Button(delete_frame, text="Delete", command=delete_info).pack()
Button(delete_frame, text="Back To Main", command=change_to_main).pack()
delete_success = Label(delete_frame, text="")
delete_success.pack()

main_menu.pack(fill='both', expand=1)


def main(username="passmanager"):
    global user_login
    user_login = username
    user_conn = config_table(user_login)
    user_conn.commit()
    user_conn.close()
    manager_screen.mainloop()


if __name__ == "__main__":
    main()
