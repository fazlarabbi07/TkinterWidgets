from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("400x400")
vertical=Scale(root,from_=0, to=200,orient=HORIZONTAL)
vertical.pack()
def click():
    #messagebox.showinfo(vertical.get()).pack()
    x=int(vertical.get())
    root.geometry('400x400')
    root.geometry(str(vertical.get())+"x"+str(vertical.get()))
 
btn=Button(root,text="Click Me!",command=click).pack()

root.mainloop()