from tkinter import *


root=Tk()

labletk1=Label(root,text="Tkinter  program")
labletk2=Label(root,text="start learning......")
#use to displaywidget in grid by grid but it is relative and provide the grid relative position
labletk1.grid(row=0,column=0)
labletk2.grid(row=1,column=4)
labletk1=Label(root,text="Tkinter  program")
labletk2=Label(root,text="start learning......")
labletk1.grid(row=1,column=5)
labletk2.grid(row=2,column=15)

# alternate way
# labletk1=Label(root,text="Tkinter  program").grid(row=0,column=0)
# labletk2=Label(root,text="start learning......").grid(row=1,column=10)
# labletk3=Label(root,text="Tkinter  program").grid(row=1,column=5)
# labletk4=Label(root,text="start learning......").grid(row=2,column=15)

root.mainloop()
