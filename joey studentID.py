from tkinter import *
import templategui2
import csv

acc=[]
def mainview():
    global mainscreen
    mainscreen = Tk()
    mainscreen.geometry("500x200")
    mainscreen.title("Account Login")
    mainscreen.configure(background = "light yellow")
    Button(text="Search", bg="light blue", width="50", height="1", font=("Calibri", 13), command = search).pack()
    Button(text="Add Student", bg="light blue", width="50", height="1", font=("Calibri", 13), command = create_contact).pack()
    Button(text="List", bg="light blue", width="50", height="1", font=("Calibri", 13), command = list).pack()
    Label(text="", bg = "light yellow").pack()
    Label(text="", bg = "light yellow").pack()

    update()


    mainscreen.mainloop()

def list():

    global  list_screen
    list_screen = Toplevel(mainscreen)
    list_screen.title("List of Students")
    list_screen.geometry('800x600')
    list_screen.configure(background="light yellow")

    Label(list_screen, text="This are the Following Students who are Enrolled", bg="light blue",font=("Calibri", 13)).pack()
    Label(list_screen, text="", bg="light yellow").pack()
    for a in acc:
        Label(list_screen, text = a.firstname+ "-" + a.lastname+ "-" + a.studentid+ "-" +a.course, bg = "light blue", width = "50", height = "1", font = ("Calibri", 13)).pack()
        Label(list_screen, text = "", bg = "light yellow").pack()



def search():

    global search_screen
    search_screen = Toplevel(mainscreen)
    search_screen.title("Search")
    search_screen.geometry('500x200')
    search_screen.configure(background="light yellow")

    global searchbox
    global selected
    global searchbox_entry
    global searchbox_label

    searchbox = StringVar()

    searchbox_label = Label(search_screen, text = "Search Student ID", bg = "light blue",font =("Calibri",13)).pack()
    searchbox_entry = Entry(search_screen, textvariable = searchbox)
    searchbox_entry.pack()
    Button(search_screen, text="Search", width=10, height=1, bg="light blue", font = ("Calibri", 13), command = lambda: gogo(searchbox)).pack()
    Button(search_screen, text="Back", width=10, height=1, bg="light blue", font = ("Calibri", 13), command = search_screen.destroy).pack()


def gogo(mama):
    selected = searchbox.get()
    global detailsscreen
    for a in acc:
        if selected == a.studentid:
            global detailsscreen
            detailsscreen = Toplevel(mainscreen)
            detailsscreen.title("Account Details")
            detailsscreen.geometry("1366x720")
            detailsscreen.configure(background="light yellow")
            Label(detailsscreen, text="First Name: " + "" + a.firstname, bg="light blue", width="50", height="1", font=("Calibri", 13)).pack()
            Label(detailsscreen, text="", bg="light yellow").pack()
            Label(detailsscreen, text="Last Name: " + "" + a.lastname, bg="light blue", width="50", height="1",font=("Calibri", 13)).pack()
            Label(detailsscreen, text="", bg="light yellow").pack()
            Label(detailsscreen, text="Personal Number: " + "" + a.personalnum, bg="light blue", width="50",height="1", font=("Calibri", 13)).pack()
            Label(detailsscreen, text="", bg="light yellow").pack()
            Label(detailsscreen, text="Student ID: " + "" + a.studentid, bg="light blue", width="50", height="1",font=("Calibri", 13)).pack()
            Label(detailsscreen, text="", bg="light yellow").pack()
            Label(detailsscreen, text="Course: " + "" + a.course, bg="light blue", width="50", height="1",font=("Calibri", 13)).pack()
            Label(detailsscreen, text="", bg="light yellow").pack()
            Button(detailsscreen, text="Edit", bg="green", width="50", height="1", font=("Calibri", 13),command=lambda:edit(mama)).pack()
            Label(detailsscreen, text="", bg="light yellow").pack()
            Button(detailsscreen, text="Delete", bg="green", width="50", height="1", font=("Calibri", 13),command=lambda:delete2(mama)).pack()
            Label(detailsscreen, text="", bg="light yellow").pack()
            Button(detailsscreen, text="Back", bg="green", width="50", height="1", font=("Calibri", 13), command=detailsscreen.destroy).pack()
            Label(detailsscreen, text="", bg="light yellow").pack()
            update()
    else:
        global else_screen
        else_screen = Toplevel(mainscreen)
        else_screen.title("Account Details")
        else_screen.geometry("500x200")
        else_screen.configure(background="light yellow")
        Label(else_screen, text="Sorry, student not found. ", bg="light blue", width="50", height="1", font=("Calibri", 13)).pack()
        Label(else_screen, text="", bg="light yellow").pack()


def delete2(mama):
    for a in acc:
        if searchbox == mama:
            acc.remove(a)
            mainscreen.destroy()
            mainview()


def create_contact():
    global register_screen
    register_screen = Toplevel(mainscreen)
    register_screen.title("Register")
    register_screen.geometry('1366x720')
    register_screen.configure(background = "light yellow")

    global firstname
    global lastname
    global personalnum
    global studentid
    global course
    global firstname_entry
    global lastname_entry
    global personalnum_entry
    global studentid_entry
    global course_entry

    firstname = StringVar()
    lastname = StringVar()
    personalnum = StringVar()
    studentid = StringVar()
    course = StringVar()


    Label(register_screen, text="Please enter details below", bg="light blue", font = ("Calibri", 13)).pack()
    Label(register_screen, text="", bg = "light yellow").pack()

    Label(register_screen, text="First Name * ", bg = "light blue", font = ("Calibri", 13)).pack()
    firstname_entry = Entry(register_screen, textvariable=firstname)
    firstname_entry.pack()
    Label(register_screen, text="Last Name * ", bg = "light blue", font = ("Calibri", 13)).pack()
    lastname_entry = Entry(register_screen, textvariable=lastname)
    lastname_entry.pack()
    Label(register_screen, text="Phone number * ", bg = "light blue", font = ("Calibri", 13)).pack()
    personalnum_entry = Entry(register_screen, textvariable=personalnum)
    personalnum_entry.pack()
    Label(register_screen, text="Student ID * ", bg = "light blue", font = ("Calibri", 13)).pack()
    studentid_entry = Entry(register_screen, textvariable=studentid)
    studentid_entry.pack()
    Label(register_screen, text="Course * ", bg = "light blue", font = ("Calibri", 13)).pack()
    course_entry = Entry(register_screen, textvariable=course)
    course_entry.pack()

    Label(register_screen, text="", bg = "light yellow").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="light blue", font = ("Calibri", 13), command = account).pack()
    Button(register_screen, text ="Cancel", width = 10, height = 1, bg = "light blue", font = ("Calibri", 13), command = register_screen.destroy).pack()
    update()


def account():

    register_screen.destroy()
    mainscreen.destroy()
    z = firstname.get()
    x = lastname.get()
    c = personalnum.get()
    n = studentid.get()
    m = course.get()
    acc.append(templategui2.template(z, x, c, n, m))
    mainview()
    #update()


def edit(marker):

    global register_screen
    register_screen = Toplevel(mainscreen)
    register_screen.title("Register")
    register_screen.geometry('1366x720')
    register_screen.configure(background = "light yellow")

    global firstname
    global lastname
    global personalnum
    global studentid
    global course
    global firstname_entry
    global lastname_entry
    global personalnum_entry
    global studentid_entry
    global course_entry

    firstname = StringVar()
    lastname = StringVar()
    personalnum = StringVar()
    studentid = StringVar()
    course = StringVar()


    Label(register_screen, text="Please enter details below", bg="light blue").pack()
    Label(register_screen, text="", bg = "light yellow").pack()

    Label(register_screen, text="First Name * ", bg = "light blue").pack()
    firstname_entry = Entry(register_screen, textvariable=firstname)
    firstname_entry.pack()
    Label(register_screen, text="Last Name * ", bg = "light blue").pack()
    lastname_entry = Entry(register_screen, textvariable=lastname)
    lastname_entry.pack()
    Label(register_screen, text="Phone number * ", bg = "light blue").pack()
    personalnum_entry = Entry(register_screen, textvariable=personalnum)
    personalnum_entry.pack()
    Label(register_screen, text="Student ID * ", bg = "light blue").pack()
    studentid_entry = Entry(register_screen, textvariable=studentid)
    studentid_entry.pack()
    Label(register_screen, text="Course * ", bg = "light blue").pack()
    course_entry = Entry(register_screen, textvariable=course)
    course_entry.pack()

    Label(register_screen, text="", bg = "light yellow").pack()
    Button(register_screen, text="Save", width=10, height=1, bg="light blue", command = lambda: save2(marker)).pack()
    Button(register_screen, text ="Cancel", width = 10, height = 1, bg = "light blue", command = register_screen.destroy).pack()
    update()


def save2(mama):
    for b in acc:
        if searchbox == mama:
            b.firstname = firstname.get()
            b.lastname = lastname.get()
            b.personalnum = personalnum.get()
            b.studentid = studentid.get()
            b.course = course.get()
            register_screen.destroy()
            detailsscreen.destroy()
            mainscreen.destroy()
            mainview()
    update()


def showother():
    with open('student.txt',newline='') as deyta:
        deita=csv.reader(deyta,delimiter=',')
        dieta=deita
        for row in dieta:
            acc.append(templategui2.template(row[0],row[1],row[2],row[3],row[4]))

def update():
    with open('student.txt','w',newline='') as deyta:
        deita=csv.writer(deyta,delimiter=',')
        for a in acc:
            deita.writerow([a.firstname]+[a.lastname]+[a.personalnum]+[a.studentid]+[a.course])

showother()
update()
mainview()
