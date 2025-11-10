from tkinter import *

# calculater
root=Tk()
# add title to main wedget
root.title("CALCULATER") 
def g():
    global sumof
    global symbol
    global mulof
    global devof
    global modof
    global total

def sum():
    g.symbol="+"
    s=e.get()
    g.sumof=float(s)
    e.delete(0,END)
def mul():
    g.symbol="*"
    s=e.get()
    g.mulof=float(s)
    e.delete(0,END)
def dev():
    g.symbol="/"
    s=e.get()
    g.devof=float(s)
    e.delete(0,END)
def mod():
    g.symbol="%"
    s=e.get()
    g.modof=float(s)
    e.delete(0,END)
def equal():
    
    if(g.symbol=="+"):
        num=int(e.get())
        e.delete(0,END)
        g.sumof=g.sumof+num
        e.insert(0,str(g.sumof))
        g.total=g.sumof
        g.sumof=0
    elif(g.symbol==""):
        num=int(e.get())
        e.delete(0,END)
        e.insert(0,str(num))
        g.total=num
    elif(g.symbol=="*"):
        num=int(e.get())
        e.delete(0,END)
        g.mulof=g.mulof*num
        e.insert(0,str(g.mulof))
        g.total=g.mulof
        g.mulof=0
    elif(g.symbol=="/"):
        num=int(e.get())
        e.delete(0,END)
        if(num!=0):
            g.devof=g.devof/num
            e.insert(0,str(g.devof))
            g.total=g.devof
        else:
            e.insert(0,"Not Exist")
            g.total=0
        
        g.devof=0
    elif(g.symbol=="%"):
        num=int(e.get())
        e.delete(0,END)
        if(num!=0):
            g.modof=g.modof%num
            e.insert(0,str(g.modof))
            g.total=g.modof
        else:
            e.insert(0,"Not Exist")
            g.total=0
        g.modof=0
        
def clear():
    e.delete(0,END)
    g.symbol==""
    g.total=0
def click(number):
    #  Whether The entry box has any character or not If there is no character then there is the only number present which I have clicked now otherwise we have to update the number with new functionality
    if(e.get()):
        total=int(e.get())
        # delete the previous number which is present in the Entry box from the starting note upto end
        e.delete(0,END)
        total=(total*10)+number
    else:
        total=number
    e.insert(0,str(total))
    g.symbol==""

e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=5,pady=5,ipady=10)

# the Lambda is useful to call a function with parameter because normally we can't use parenthesis But to pass a parameter we have to use parenthesis That's why Lambda is used
btn1=Button(root,text="1",padx=25,pady=20,command=lambda: click(1))
btn2=Button(root,text="2",padx=25,pady=20,command=lambda: click(2))
btn3=Button(root,text="3",padx=25,pady=20,command=lambda: click(3))
btn4=Button(root,text="4",padx=25,pady=20,command=lambda: click(4))
btn5=Button(root,text="5",padx=25,pady=20,command=lambda: click(5))
btn6=Button(root,text="6",padx=25,pady=20,command=lambda: click(6))
btn7=Button(root,text="7",padx=25,pady=20,command=lambda: click(7))
btn8=Button(root,text="8",padx=25,pady=20,command=lambda: click(8))
btn9=Button(root,text="9",padx=25,pady=20,command=lambda: click(9))
btn0=Button(root,text="0",padx=25,pady=20,command=lambda: click(0))
btnplus=Button(root,text="+",padx=25,pady=20,bg="yellow",command=sum)
btnmul=Button(root,text="*",padx=25,pady=20,bg="yellow",command=mul)
btndev=Button(root,text="/",padx=25,pady=20,bg="yellow",command=dev)
btnmod=Button(root,text="%",padx=25,pady=20,bg="yellow",command=mod)
btnequal=Button(root,text="=",padx=65,pady=20,bg="green",fg="white",command=equal)
btnclear=Button(root,text="clear",padx=55,pady=20,bg="red",fg="white",command=clear)

btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)
btn7.grid(row=3,column=0)
btn8.grid(row=3,column=1)
btn9.grid(row=3,column=2)
btn0.grid(row=4,column=0)
btnclear.grid(row=5,column=1,columnspan=2)
btnplus.grid(row=5,column=0)
btnmul.grid(row=4,column=1)
btndev.grid(row=4,column=2)
btnmod.grid(row=6,column=0)
btnequal.grid(row=6,column=1,columnspan=2)

root.mainloop()
