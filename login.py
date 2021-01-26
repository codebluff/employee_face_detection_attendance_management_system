from tkinter import *
from tkinter import messagebox
import pymysql

root = Tk()
root.title("Attendance Using Face Recognization")
root.config(bg="white")
root.geometry("550x340+480+230")
root.resizable(False, False)




def lgndb():
    if usernameentry.get() == "" or passentry.get() == "":
        messagebox.showerror('Error', "All fields are required")
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="", database="project")
            cur = con.cursor()
            cur.execute("select * from login where username=%s and password=%s", (usernameentry.get(), passentry.get()))
            row = cur.fetchall()
            if row == ():
                messagebox.showerror("Error", 'Invalid')
            else:
                root.destroy()
                import main

        except Exception as e:
            messagebox.showerror("Error", f"Error due to:{str(e)}")


frame = Frame(root, bg='white', borderwidth=1)
frame.place(x=150, y=150, width=500, height=340)

title = Label(root, text="Login Here", font=('Impact', 30), bg='white', fg="#d77337")
title.place(x=100, y=20)
desc = Label(root, text="HR Employee Login Area", font=('Goudy old style', 12), bg='white', fg="#d25d17")
desc.place(x=100, y=70)

usernamelabel = Label(root, text="Username", font=('Goudy old style', 15, 'bold'), foreground="gray", bg='white')
usernamelabel.place(x=100, y=110)
usernameval = StringVar()
usernameentry = Entry(root, font=('times new roman', 15), bd=1, textvariable=usernameval, bg='lightgray')
usernameentry.place(x=100, y=140, width=300, height=25)

passlabel = Label(root, text="Password", font=('Goudy old style', 15, 'bold'), foreground="gray", bg='white')
passlabel.place(x=100, y=180)
passval = StringVar()
passentry = Entry(root, font=('times new roman', 15), bd=1, show="*", textvariable=passval, bg='lightgray')
passentry.place(x=100, y=210, width=300, height=25)

loginbtn = Button(root, text='Login', width=10, font=('times new roman', 12, 'bold'), cursor="hand2", relief=RIDGE,
                  borderwidth=1, bg='#d77337', foreground="white", bd=1, command=lgndb)
loginbtn.place(x=100, y=270)

root.mainloop()