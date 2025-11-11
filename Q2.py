from tkinter import *

root = Tk()

e1=Entry(root,width=30,borderwidth=5)
e1.insert(0,"enter your name :")

e2=Entry(root,width=30,borderwidth=5)
e2.insert(0,"enter your ph no :")

e3=Entry(root,width=30,borderwidth=5)
e3.insert(0,"enter your email id:")

e1.grid(row=0,column=0,columnspan=4)
e2.grid(row=1,column=0,columnspan=4)
e3.grid(row=2,column=0,columnspan=4)

def submit():
    s1=str(e1.get())
    s2=str(e2.get())
    s3=str(e3.get())
    l1=Label(root,text=s1)
    l2=Label(root,text=s2)
    l3=Label(root,text=s3)
    l1.grid(row=4,column=2)
    l2.grid(row=5,column=2)
    l3.grid(row=6,column=2)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e1.insert(0,"enter your name :")
    e2.insert(0,"enter your ph no :")
    e3.insert(0,"enter your email id:")


s=Button(root,text="Submit",command=submit)
s.grid(row=3,column=2)





root.mainloop()