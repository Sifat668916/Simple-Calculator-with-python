from tkinter import *
root = Tk()
root.title("Simple Calculator")
e = Entry(root,width=50,borderwidth=5)
# e.insert(0,"Enter your number:")
e.grid(column=0,row=0,columnspan=3,padx=10,pady=10)
def clicked(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))
def add():
    global a 
    global math
    math = "addition"
    a = int(e.get())
    e.delete(0,END)
def sub():
    global a 
    global math
    math = "sub"
    a = int(e.get())
    e.delete(0,END)
def mul():
    global a 
    global math
    math = "mul"
    a = int(e.get())
    e.delete(0,END)
def div():
    global a 
    global math
    math = "addition"
    a = int(e.get())
    e.delete(0,END)


def equal():

    b = int(e.get())
    e.delete(0,END)
    if(math == "addition"):
        e.insert(0, int(a) + int(b))
    elif(math == "sub"):
        e.insert(0, int(a) - int(b))
    elif(math == "mul"):
        e.insert(0, int(a) * int(b))
    elif(math == "div"):
        e.insert(0, int(a) / int(b))




    
def clear():
    e.delete(0,END)
btn1 = Button(root,text = "1",padx=45,pady=30,command=lambda :clicked(1))
btn2 = Button(root,text = "2",padx=45,pady=30,command=lambda: clicked(2))
btn3 = Button(root,text = "3",padx=45,pady=30,command=lambda: clicked(3))
btn4 = Button(root,text = "4",padx=45,pady=30,command=lambda: clicked(4))
btn5 = Button(root,text = "5",padx=45,pady=30,command=lambda: clicked(5))
btn6 = Button(root,text = "6",padx=45,pady=30,command=lambda: clicked(6))
btn7 = Button(root,text = "7",padx=45,pady=30,command=lambda: clicked(7))
btn8 = Button(root,text = "8",padx=45,pady=30,command=lambda: clicked(8))
btn9 = Button(root,text = "9",padx=45,pady=30,command=lambda: clicked(9))
btn0 = Button(root,text = "0",padx=45,pady=30,command=lambda: clicked(0))
btnadd = Button(root,text = "+",padx=45,pady=30,command= add)
btnmul = Button(root,text = "*",padx=45,pady=30,command= mul)
btnsub = Button(root,text = "-",padx=45,pady=30,command= sub)
btndiv = Button(root,text = "-",padx=45,pady=30,command= div)
btnclear = Button(root,text = "Clear",padx=88,pady=30,command=clear)
btnresult = Button(root,text = "=",padx=98,pady=30,command= equal)


#put the buttons on the screen
btn0.grid(row=1,column=0)
btn1.grid(row=1,column=1)
btn2.grid(row=1,column=2)

btn3.grid(row=2,column=0)
btn4.grid(row=2,column=1)
btn5.grid(row=2,column=2)

btn6.grid(row=3,column=0)
btn7.grid(row=3,column=1)
btn8.grid(row=3,column=2)
btn9.grid(row=4,column=0)

btnadd.grid(row=4,column=1)
btnsub.grid(row=4,column=2)
btnmul.grid(row=5,column=0)
btndiv.grid(row=6,column=0)

btnclear.grid(row=5,column=1,columnspan=2)
btnresult.grid(row=6,column=1,columnspan=2)

root.mainloop()