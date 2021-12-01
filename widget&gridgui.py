from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry=("655x333")
root.title("widget and grid gui")
def submit():
    print(firstnamevalue.get())
    print(surnamevalue.get())
    messagebox.showinfo("Message","submitted")
firstname=Label(root,text="firstname")
firstname.grid(row=0,padx=6)
surname=Label(root,text="surname")
surname.grid(row=1,padx=6)
# variable classes in tkinter
# BooleanVar , DoubleVar , StringVar , IntVar
firstnamevalue= StringVar()
surnamevalue= StringVar()
firstnameentry= Entry(root,textvariable= firstnamevalue)
surnameentry= Entry(root,textvariable= surnamevalue)
firstnameentry.grid(row=0,column=1)
surnameentry.grid(row=1,column=1)
btn=Button(text ="submit",command=submit,padx=6)
btn.grid(row=4,column=1)
root.mainloop()
