from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("this is for title")
# add icon 
# root.iconbitmap("path of the icon file")

buttonquite=Button(root,text="exit program",command=root.quit)
buttonquite.pack()
# Add or display any image As a label

myimg=ImageTk.PhotoImage(Image.open("C:/Users/soumyadeep DEY/OneDrive/Pictures/134042130083524214.jpg"))
mylabel=Label(image=myimg,width=50,height=50)
mylabel.pack()

root.mainloop()
