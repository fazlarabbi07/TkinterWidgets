from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
root=Tk()
root.title("Dialog Box")
root.iconbitmap("photos/image.ico")
#initialdir indicate the directory where to open the dialog box
def open():
    global my_image
    root.filename=filedialog.askopenfilename(initialdir="C:/Users/ii/Desktop/Python/Dialog_box/photos",title="Selece you photo ",filetypes=(("png file","*.png"),("Al l file","*.*")))
    my_image=ImageTk.PhotoImage(Image.open( root.filename))
    my_label=Label(image=my_image).pack()

my_button=Button(root,text="SEE Photos",command=open).pack()




root.mainloop()