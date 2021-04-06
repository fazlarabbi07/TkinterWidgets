from tkinter import *
from tkinter import messagebox
import sqlite3
root=Tk()
root.title("Creating DB")
root.geometry("400x400")

# Database
# Creating DB
conn=sqlite3.connect('address_book.db')
# create cursor
c=conn.cursor()
# Create the table one time please  
#Creating table
# Table should be create only one time
'''c.execute("""CREATE TABLE addresses(
    first_name text,
    last_name text,
    addredd text,
    city text,
    state text,
    zipcode interger)""")
'''
'''Creating Widgets'''
first_name=Entry(root,width=30)
last_name=Entry(root,width=30)
address=Entry(root,width=30)
city=Entry(root,width=30)
state=Entry(root,width=30)
zipcode=Entry(root,width=30)
#Widget Show with grid


first_name.grid(row=0,column=1,padx=30,pady=(15,0))
last_name.grid(row=1,column=1,padx=30,pady=5)
address.grid(row=2,column=1,padx=30,pady=5)
city.grid(row=3,column=1,padx=30,pady=5)
state.grid(row=4,column=1,padx=30,pady=5)
zipcode.grid(row=5,column=1,padx=30,pady=15)
'''Creating Text Box Label'''
first_name_label=Label(root,text="First Name: ")
first_name_label.grid(row=0,column=0,padx=10,pady=(15,0))

last_name_label=Label(root,text="Last Name: ")
last_name_label.grid(row=1,column=0,padx=10)

address_name_label=Label(root,text="Address: ")
address_name_label.grid(row=2,column=0,padx=10)

city_name_label=Label(root,text="City: ")
city_name_label.grid(row=3,column=0,padx=10)

state_name_label=Label(root,text="State: ")
state_name_label.grid(row=4,column=0,padx=10)

zipcode_name_label=Label(root,text="Zipcode: ")
zipcode_name_label.grid(row=5,column=0,padx=10)

delete_label=Label(root,text="Delete ID")
delete_label.grid(row=8,column=0)
delete_entry=Entry(root,width=30)
delete_entry.grid(row=8,column=1)
# Submit Button Functionality
def submit():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor()
    #Insert into table
    c.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)",
    
            {
                'f_name':first_name.get(),
                'l_name':last_name.get(),
                'address':address.get(),
                'city':city.get(),
                'state':state.get(),
                'zipcode':zipcode.get()


            } )
   
    messagebox.showinfo("Report","Submission is Completed")
    conn.commit()
    #Close Connection
    conn.close()

    #Clear the Entry after the submit button is clicked 
    first_name.delete(0,END)
    last_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)

#Query Button functionality
def query():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor() 
    #Query the data base
    c.execute("SELECT *,oid FROM addresses")
    print_record=''
    record=c.fetchall()
    for records in record:
        print_record+=str(records[0]) +" "+str(records[1])+" " +str(records[6])+ "\n"

    query_label=Label(root,text=print_record)
    query_label.grid(row=8,column=0,columnspan=2)



    conn.commit()
    #Close Connection
    conn.close()
#Delete Button functionality
def delete():
    conn=sqlite3.connect('address_book.db')
    c=conn.cursor() 
    c.execute("DELETE FROM addresses WHERE oid="+ delete_entry.get())

    conn.commit()
    #Close Connection
    conn.close()
    delete_entry.delete(0,END)

# Creating Submit Button
submit_button=Button(root,text="Add Record to Database",command=submit)
submit_button.grid(row=6,column=1,columnspan=2,ipady=5)
#Creating Query Button
query_button=Button(root,text="Show Records",command=query)
query_button.grid(row=7,column=1,columnspan=2,pady=5)
#Creating Delete Button
delete_button=Button(root,text="Delete Record",command=delete)
delete_button.grid(row=9,column=1,columnspan=2,ipady=5)
#commit change
conn.commit()

#Close Connection
conn.close()



root.mainloop()