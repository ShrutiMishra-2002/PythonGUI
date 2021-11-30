from tkinter import *
root=Tk()
root.geometry=("644x434")
root.title("editor gui")
frame=Frame(root, bg="blue", borderwidth=7, relief=SUNKEN)
frame.pack(side=LEFT,fill=Y)
frame1=Frame(root, bg="blue", borderwidth=7, relief=SUNKEN)
frame1.pack(anchor="ne",fill=X)
l=Label(frame,text="python gui",padx=38)
l.pack(pady=352)
l1=Label(frame1,text="File    Edit    Selection    View     Go     Run    Terminal    Help", pady=18)
l1.pack()
photo=PhotoImage(file="py.png")
photo_label = Label(image=photo , height=500 , width=500)
photo_label.pack(side = "bottom",anchor="n")

root.mainloop()


