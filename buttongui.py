from tkinter import *
from tkinter import messagebox
Root = Tk()
Root.geometry("644x434")
Root.minsize(733,435)
Root.maxsize(1200,644)
Root.title("button gui")
def btnclick():
   messagebox.showinfo("Message","java is clicked")
   print("hello java users")
def btnclick1():
   messagebox.showinfo("Message","python is clicked")
   print("hello python users")
def btnclick2():
   messagebox.showinfo("Message","C is clicked")
   print("hello C users")
def btnclick3():
   messagebox.showinfo("Message","Cpp is clicked")
   print("hello Cpp users")
l=Label(text="THIS IS A BUTTON GUI WINDOW!!")
l.pack()
btn1=Button(Root, borderwidth=6, text="java", relief=SUNKEN, command=btnclick, padx=38)
btn1.pack(side=LEFT,padx=20)
btn2=Button(Root, borderwidth=6, text="python", relief=SUNKEN, command=btnclick1, padx=38)
btn2.pack(side=LEFT,padx=20)
btn3=Button(Root, borderwidth=6, text="C", relief=SUNKEN, command=btnclick2, padx=38)
btn3.pack(side=LEFT,padx=20)
btn4=Button(Root, borderwidth=6, text="Cpp", relief=SUNKEN, command=btnclick3, padx=38)
btn4.pack(side=LEFT,padx=20)


Root.mainloop()
