from tkinter import *


root=Tk()
# taking input
e=Entry(root,width=50,borderwidth=5,fg="red",bg="yellow")
e.pack()
# insert help to insert text in any relative position where 0 is the relative position 
e.insert(0,"enter your name :")
def clickbtn():

    # e.get is to get the input
    lbl=Label(root,text=e.get())
    lbl.pack()

btn=Button(root,text="enter name! :)",command=clickbtn,fg="red",bg="yellow")
btn.pack()
root.mainloop()
