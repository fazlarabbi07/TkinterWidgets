from tkinter import *
root=Tk()
root.geometry("400x400")
#check box
#val=IntVar()
#for string
val=StringVar()
c=Checkbutton(root,text="Check Me!",variable=val,onvalue="on",offvalue="off")
#If we take String for on value and off value then we must need to use Deselect function
c.deselect()
c.pack(anchor=W)
#Function
def clicklabel():
    #label
    my_label=Label(root,text=str(val.get())).pack()

#button
my_btn=Button(root,text="Show Selection",command=clicklabel)
my_btn.pack()
root.mainloop()

