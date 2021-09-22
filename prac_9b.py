# Message in python
from tkinter import*
root = Tk()
var  = StringVar()
label = Message(root, textvariable=var, relief=RAISED)
var.set("Hey! How are you doing?")
label.pack()
root.mainloop()

# Button in Python
import tkinter
import tkinter.messagebox
top = tkinter.Tk()
def helloCallBack():
    tkinter.MessageBox.showinfo("Hello Python","Hello World")
B = tkinter.Button(top,text="Hello",command = helloCallBack)
B.pack()
top.mainloop()

# Entry in Python
top = Tk()
l1 = Label(top, text="User Name")
l1.pack(side=LEFT)
e1 = Entry(top, bd=5)
e1.pack(side=RIGHT)
top.mainloop()

# CheckButton in python
top = tkinter.Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
c1 = Checkbutton(top, text="Music", variable = CheckVar1, onvalue = 1, offvalue = 0, height = 5, width = 20)
c2 = Checkbutton(top, text="Video", variable = CheckVar2, onvalue = 1, offvalue = 0, height = 5, width = 20)
c1.pack()
c2.pack()
top.mainloop()

# Radio Button in python 
def sel():
    selection = "You selected the option"+str(var.get())
    label.config(text = selection)
root = Tk()
var = IntVar()
r1 = Radiobutton(root, text = "Option 1", variable = var, value = 3, command = sel)
r1.pack(anchor=W)
r2 = Radiobutton(root, text = "Option 2", variable = var, value = 3, command = sel)
r2.pack(anchor=W)
r3 = Radiobutton(root, text = "Option 3", variable = var, value = 3, command = sel)
r3.pack(anchor=W)
label = Label(root)
label.pack()
root.mainloop()

# Scale in python
def sel():
    selection = "Value = "+str(var.get())
    label.config(text = selection)
root = Tk()
var = DoubleVar()
scale = Scale(root, variable = var)
scale.pack(anchor = CENTER)
button = Button(root, text = "Get scale Value",command=sel)
button.pack(anchor=CENTER)
label = Label(root)
root.mainloop()