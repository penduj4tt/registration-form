from tkinter import *
from tkinter import messagebox
from mysql import connector

def database():
    conn = connector.connect(user='root',password='0356',host='localhost',port='3306',database='sukhi')
    mycursor = conn.cursor()
    mycursor.execute("insert into registration values(%s,%s,%s,%s,%s,%s)",(sr_no.get(), name.get(), roll_no.get(), address.get(), branch.get(), gender.get()))
    messagebox.showinfo("Info","Submitted")
    conn.commit()

root = Tk()
root.geometry('500x500')
root.title("Registration Form")
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="S No",width=20,font=("bold", 10))
label_1.place(x=80,y=130)
sr_no = Entry(root)
sr_no.place(x=240,y=130)

label_2 = Label(root, text="Name",width=20,font=("bold", 10))
label_2.place(x=80,y=180)
name = Entry(root)
name.place(x=240,y=180)

label_3 = Label(root, text="Address",width=20,font=("bold", 10))
label_3.place(x=80,y=230)
address = Entry(root)
address.place(x=240,y=230)

label_4 = Label(root, text="Roll No",width=20,font=("bold", 10))
label_4.place(x=80,y=280)
roll_no = Entry(root)
roll_no.place(x=240,y=280)

label_5 = Label(root, text="Gender",width=20,font=("bold", 10))
label_5.place(x=80,y=330)
gender = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=gender, value=1).place(x=235,y=330)
Radiobutton(root, text="Female",padx = 20, variable=gender, value=2).place(x=290,y=330)

label_6 = Label(root, text="Branch",width=20,font=("bold", 10))
label_6.place(x=80,y=380)
branch = StringVar(root)
branch.set("Select") # default value

w = OptionMenu(root, branch, "CSE", "IT", "ECE", "ME", "CE")
w.pack()
w.place(x=240,y=380)


Button(root, text='Submit',width=20,bg='blue',fg='white',command=database).place(x=180,y=430)
# it is use for display the registration form on the window
root.mainloop()
print("registration form  seccussfully created...")
