from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("this is for title")
# Add or display any image As a label

myimg1=ImageTk.PhotoImage(Image.open("C:/Users/soumyadeep DEY/OneDrive/Pictures/134042130083524214.jpg"))
myimg2=ImageTk.PhotoImage(Image.open("C:/Users/soumyadeep DEY/OneDrive/Pictures/134042130083524214.jpg"))
myimg3=ImageTk.PhotoImage(Image.open("C:/Users/soumyadeep DEY/OneDrive/Pictures/134042130083524214.jpg"))
myimg4=ImageTk.PhotoImage(Image.open("C:/Users/soumyadeep DEY/OneDrive/Pictures/134042130083524214.jpg"))
myimg5=ImageTk.PhotoImage(Image.open("C:/Users/soumyadeep DEY/OneDrive/Pictures/134042130083524214.jpg"))
imagelist=[myimg1,myimg2,myimg3,myimg4,myimg5]

mylabel1=Label(image=myimg1,width=50,height=50)
mylabel2=Label(image=myimg2,width=50,height=50)
mylabel3=Label(image=myimg3,width=50,height=50)
mylabel4=Label(image=myimg4,width=50,height=50)
mylabel5=Label(image=myimg5,width=50,height=50)

mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=0)
mylabel3.grid(row=2,column=1)
mylabel4.grid(row=1,column=1)
mylabel5.grid(row=2,column=0)

root.mainloop()
