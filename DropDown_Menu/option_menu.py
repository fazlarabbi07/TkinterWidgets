from tkinter import *
root=Tk()
root.geometry("400x400")
def click():

    my_lebel=Label(root,text="You have Selected "+val.get()).pack()
#Button Creation
my_button=Button(root,text="Select Your Day",command=click)
my_button.pack()
#StringVar is a method to get the value of "val"
val=StringVar()
dayList=["Friday","Saturday","Sunday","Monday","Tuesday","Wednesday","Thurday"]\
# "*" is use to represent the day in vertically
dropmenu=OptionMenu(root,val,*dayList)
val.set(dayList[5])
dropmenu.pack()



root.mainloop()