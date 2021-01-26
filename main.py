from tkinter import *
from tkinter.ttk import Treeview, Combobox
from tkinter import ttk
import pymysql
from tkinter import messagebox

root = Tk()
root.title("Department and Management")
root.config(bg="dark slate gray")
root.geometry("1500x800+0+0")
root.resizable(False, False)


# function
def addemp():
    print("Employee added")


def updateemp():
    print("Employee Updated")


def deleteemp():
    print("Employee Deleted")


def addphoto():
    print("")


def updatephoto():
    print("")


def adddept():
    try:
        con = pymysql.connect(host="localhost", user="root", password="", database="project")
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS DEPARTMENT (DEPARTMENT_NAME VARCHAR(255))")
        cur.execute("SELECT * FROM DEPARTMENT")
        cur.execute("INSERT INTO DEPARTMENT('DEPARTMENT_NAME') VALUES ('%s')", (deptnameentry.get()))
    except Exception as e:
        messagebox.showerror("Error", f"Error due to:{str(e)}")


def deletedept():
    try:
        con = pymysql.connect(host="localhost", user="root", password="", database="project")
        cur = con.cursor()
        cur.execute("DELETE FROM DEPARTMENT WHERE DEPARTMENT_NAME = '(%s)'", (deptnameentry.get()))
        con.close()
        cur.close()
    except Exception as e:
        messagebox.showerror("Error", f"Error due to:{str(e)}")


# Frames
DataEntryFrame = Frame(root, bg='red', relief=GROOVE, borderwidth=1)
DataEntryFrame.place(x=20, y=100, width=580, height=680)

ShowDataFrame = Frame(root, bg='red', relief=GROOVE, borderwidth=1)
ShowDataFrame.place(x=620, y=100, width=860, height=680)

tableFrame = Frame(ShowDataFrame, bg='white', relief=GROOVE, borderwidth=1)
tableFrame.place(x=10, y=15, width=835, height=350)

DptFrame = Frame(ShowDataFrame, bg='white', relief=GROOVE, borderwidth=1)
DptFrame.place(x=10, y=380, width=835, height=280)

DpttabFrame = Frame(ShowDataFrame, bg='white', relief=GROOVE, borderwidth=2)
DpttabFrame.place(x=550, y=430, width=280, height=220)

# Mainlabel
label = Label(root, text="Manage Employee and Department", font=('', 40), bg='mint cream', relief=GROOVE, borderwidth=1)
label.place(x=0, y=10, width=1500)

# Entry label
label = Label(DataEntryFrame, text="Manage Employee", font=('arial', 25, 'bold'), foreground="white", width=22,
              bg='red')
label.place(x=70, y=30)

namelabel = Label(DataEntryFrame, text="Name:", font=('arial', 16), foreground="white", width=0, bg='red')
namelabel.place(x=25, y=100)

genderlabel = Label(DataEntryFrame, text="Gender:", font=('arial', 16), foreground="white", width=0, bg='red')
genderlabel.place(x=25, y=150)

empidlabel = Label(DataEntryFrame, text="Employee Id:", font=('arial', 16), foreground="white", width=0, bg='red')
empidlabel.place(x=25, y=200)

departmentlabel = Label(DataEntryFrame, text="Department:", font=('arial', 16), foreground="white", width=0, bg='red')
departmentlabel.place(x=25, y=250)

contactlabel = Label(DataEntryFrame, text="Contact No:", font=('arial', 16), foreground="white", width=0, bg='red')
contactlabel.place(x=25, y=300)

doblabel = Label(DataEntryFrame, text="D.O.B:", font=('arial', 16), foreground="white", width=0, bg='red')
doblabel.place(x=25, y=350)

dojlabel = Label(DataEntryFrame, text="Date of Joining:", font=('arial', 16), foreground="white", width=0, bg='red')
dojlabel.place(x=25, y=400)

frame = Frame(DataEntryFrame, bg='white', relief=GROOVE, borderwidth=1)
frame.place(x=25, y=500, width=500, height=100)
# Buttons
addbtn = Button(DataEntryFrame, text='Add', width=10, font=('arial', 12, 'bold'), relief=RIDGE, borderwidth=1,
                bg='dark slate gray', foreground="white", command=addemp)
addbtn.place(x=40, y=515)

updatebtn = Button(DataEntryFrame, text='Update', width=10, font=('arial', 12, 'bold'), relief=RIDGE, borderwidth=1,
                   bg='dark slate gray', foreground="white", command=updateemp)
updatebtn.place(x=160, y=515)

deletebtn = Button(DataEntryFrame, text='Delete', width=10, font=('arial', 12, 'bold'), relief=RIDGE, borderwidth=1,
                   bg='dark slate gray', foreground="white", command=deleteemp)
deletebtn.place(x=280, y=515)

clearbtn = Button(DataEntryFrame, text='Clear', width=10, font=('arial', 12, 'bold'), relief=RIDGE, borderwidth=1,
                  bg='dark slate gray', foreground="white")
clearbtn.place(x=400, y=515)

addphotobtn = Button(DataEntryFrame, text='Add Photo', width=22, font=('arial', 12, 'bold'), relief=RIDGE,
                     borderwidth=1, bg='gold', foreground="black", command=addphoto)
addphotobtn.place(x=40, y=560)

updatephotobtn = Button(DataEntryFrame, text='Update Photo Sample', width=22, font=('arial', 12, 'bold'), relief=RIDGE,
                        borderwidth=1, bg='gold', foreground="black", command=updatephoto)
updatephotobtn.place(x=280, y=560)

# Entry
nameval = StringVar()
genderval = IntVar()
idval = StringVar()
comboval = StringVar()
contactval = StringVar()
dobval = StringVar()
dojval = StringVar()

nameentry = Entry(DataEntryFrame, font=('arial', 12), bd=2, textvariable=nameval, width=25)
nameentry.place(x=250, y=100)

r1 = Radiobutton(DataEntryFrame, text="Male", padx=20, font=('arial', 12), bg='red', value=1, variable=genderval)
r1.place(x=250, y=150)
r2 = Radiobutton(DataEntryFrame, text="Female", padx=20, font=('arial', 12), bg='red', value=2, variable=genderval)
r2.place(x=350, y=150)

identry = Entry(DataEntryFrame, font=('arial', 12), bd=3, textvariable=idval, width=25)
identry.place(x=250, y=200)

v = ["HR", "Sales & Marketing", "Production"]
combo = Combobox(DataEntryFrame, value=v)
combo.place(x=250, y=250)

contactentry = Entry(DataEntryFrame, font=('arial', 12), bd=3, textvariable=contactval, width=25)
contactentry.place(x=250, y=300)

dobentry = Entry(DataEntryFrame, font=('arial', 12), bd=3, textvariable=dobval, width=25)
dobentry.place(x=250, y=350)

dojentry = Entry(DataEntryFrame, font=('arial', 12), bd=3, textvariable=dojval, width=25)
dojentry.place(x=250, y=400)

# Right frame Tabular form
style = ttk.Style()
style.configure('Treeview.Heading', font=('arial', 10, 'bold'))
scroll_x = Scrollbar(tableFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(tableFrame, orient=VERTICAL)
table = Treeview(tableFrame,
                 column=('Name', 'Gender', 'Employee Id', 'Department', 'Contact No.', 'D.O.B', 'Date of Joining')
                 , yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=table.xview)
scroll_y.config(command=table.yview)
table.heading('Name', text='Name')
table.heading('Gender', text='Gender')
table.column('Gender', width=80)
table.heading('Employee Id', text='Employee Id')
table.column('Employee Id', width=100)
table.heading('Department', text='Department')
table.heading('Contact No.', text='Contact No.')
table.column('Contact No.', width=150)
table.heading('D.O.B', text='D.O.B')
table.column('D.O.B', width=150)
table.heading('Date of Joining', text='Date of Joining')
table.column('Date of Joining', width=150)
table['show'] = 'headings'
table.pack(fill=BOTH, expand=1)

# Right Frame Department form
mainlabel = Label(DptFrame, text="Department Management", font=('', 12, 'bold'), padx=5, bg='white', relief=GROOVE,
                  borderwidth=0)
mainlabel.place(x=0, y=10, width=250)

deptlabel = Label(DptFrame, text="Department Name", font=('', 15, 'bold'), padx=5, bg='white', relief=GROOVE,
                  borderwidth=0)
deptlabel.place(x=30, y=100, width=250)

deptvar = StringVar()
deptnameentry = Entry(DptFrame, font=('arial', 12), bd=2, textvariable=deptvar, width=20)
deptnameentry.place(x=300, y=100)

# Department Frame Button

addbtndept = Button(DptFrame, text='Add', width=10, font=('arial', 12, 'bold'), relief=RIDGE, borderwidth=1,
                    bg='dark slate gray', foreground="white", command=adddept)
addbtndept.place(x=180, y=200)

deletebtndept = Button(DptFrame, text='Delete', width=10, font=('arial', 12, 'bold'), relief=RIDGE, borderwidth=1,
                       bg='dark slate gray', foreground="white", command=deletedept)
deletebtndept.place(x=300, y=200)

# Department Tabular form
style = ttk.Style()
style.configure('Treeview.Heading', font=('arial', 10, 'bold'))
scroll_x = Scrollbar(DpttabFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(DpttabFrame, orient=VERTICAL)
table = Treeview(DpttabFrame, column=('Id', 'Department'),
                 yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=table.xview)
scroll_y.config(command=table.yview)
table.heading('Id', text='Id')
table.column('Id', width=50)
table.heading('Department', text='Department')
table['show'] = 'headings'
table.pack(fill=BOTH, expand=1)

root.mainloop()
