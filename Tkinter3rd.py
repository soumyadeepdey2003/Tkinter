from tkinter import *


root=Tk()

# button creation
# btn=Button(root,text="click here :)")


#  state=DISABLED make the button unclickable
# padx for x axis padding and pady for y axis pading 
# btn=Button(root,text="click here :)",state=DISABLED,padx=10,pady=10)


def clickbtn():
    lbl=Label(root,text="button has been clicked ")
    lbl.pack()
# command help to add functionality but the function parenthesis should not be added and the function will only call when the button is clicked
# fg is used to colors of the button text and bg for background color
btn=Button(root,text="click here! :)",command=clickbtn,fg="red",bg="yellow")
btn.pack()

root.mainloop()
