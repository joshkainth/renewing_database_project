from tkinter import *
from tkinter import ttk
from tkinter import Radiobutton
from tkinter import messagebox
import mysql.connector
import pandas as pd

def main_gui():
    global window
    window = Tk()
    window.title("Database Project")
    window.geometry("625x270")
    Lbl1 = Label(window, text="Hello User :) ", font="Arial 18").place(x=240, y=10)
    Lbl2 = Label(window, text="What you want to do ?", font="Arial 18").place(x=185, y=50)

    Btn1 = Button(window, text="Insert Data", command=onclick_main_add, font="Arial 14")
    Btn1.place(x=10, y=210)

    Btn2 = Button(window, text="Update Data", command=onclick_main_update, font="Arial 14")
    Btn2.place(x=125, y=210)

    Btn3 = Button(window, text="Delete Data", command=onclick_main_delete, font="Arial 14")
    Btn3.place(x=255, y=210)

    Btn4 = Button(window, text="View Data", command=onclick_main_view, font="Arial 14")
    Btn4.place(x=378, y=210)

    Btn17 = Button(window, text="Exit Program", command=exit_main_window, font="Arial 14")
    Btn17.place(x=488, y=210)

    window.mainloop()

def add_gui():  
    global entryName,entryEmail,entryPhone,entryCity,entryState
    global add_window
    add_window = Tk()
    add_window.title("Save Data")
    add_window.geometry("500x270")

    Lb1 = Label(add_window, text="Enter the Customer Name : ", font="Arial 14").place(x=10, y=10)
    entryName = Entry(add_window, width=22, font="Arial 14")
    entryName.place(x=250, y=10)

    Lb2 = Label(add_window, text="Enter the Customer Email : ", font="Arial 14").place(x=10, y=50)
    entryEmail = Entry(add_window, width=22, font="Arial 14")
    entryEmail.place(x=250, y=50)

    Lb3 = Label(add_window, text="Enter Phone Number : ", font="Arial 14").place(x=10, y=90)
    entryPhone = Entry(add_window, width=22, font="Arial 14")
    entryPhone.place(x=250, y=90)

    Lb4 = Label(add_window, text="Enter City : ", font="Arial 14").place(x=10, y=130)
    entryCity = Entry(add_window, width=22, font="Arial 14")
    entryCity.place(x=250, y=130)

    Lb5 = Label(add_window, text="Enter State : ", font="Arial 14").place(x=10, y=170)
    entryState = Entry(add_window, width=22, font="Arial 14")
    entryState.place(x=250, y=170)

    Btn5 = Button(add_window, text="Cancel", command=exit_add_window, font="Arial 14")
    Btn5.place(x=410, y=210)

    Btn6 = Button(add_window, text="Save Data", command=add, font="Arial 14")
    Btn6.place(x=300, y=210)

    Btn7 = Button(add_window, text="Back To Main Menu", command=onclick_insert, font="Arial 14")
    Btn7.place(x=110, y=210)
    add_window.mainloop()


def update_gui():
    global update_existingName, newName
    global update_existingEmail, newEmail
    global update_existingPhone, newPhone
    global Rbtn1, Rbtn2, Rbtn3, Rbtn4, Rbtn5, Rbtn6
    global radio, radio12
    global update_window

    update_window = Tk()
    update_window.title("Updating Data")
    update_window.geometry("500x440")
    radio = IntVar()
    radio12 = IntVar()

    Lbl1 = Label(update_window, text="Hey User! What thing you want To Update?", font="Arial 16")
    Lbl1.place(x=5, y=5)

    Lbl8 = Label(update_window, text="From which option would you want to update !!", font="Arial 16")
    Lbl8.place(x=5, y=70)

    Lbl2 = Label(update_window, text="Enter New Name -> ", font="Arial 16").place(x=10, y=145)
    newName = Entry(update_window, width=22, font="Arial 14", state=DISABLED)
    newName.place(x=250, y=145)

    Lbl3 = Label(update_window, text="Enter New Email -> ", font="Arial 16").place(x=10, y=185)
    newEmail = Entry(update_window, width=22, font="Arial 14", state=DISABLED)
    newEmail.place(x=250, y=180)

    Lbl4 = Label(update_window, text="Enter New Phone -> ", font="Arial 16").place(x=10, y=225)
    newPhone = Entry(update_window, width=22, font="Arial 14", state=DISABLED)
    newPhone.place(x=250, y=225)

    Lbl5 = Label(update_window, text="Enter Existing Name -> ", font="Arial 16").place(x=10, y=265)
    update_existingName = Entry(update_window, width=22, font="Arial 14", state=DISABLED)
    update_existingName.place(x=250, y=265)

    Lbl6 = Label(update_window, text="Enter Existing Email -> ", font="Arial 16").place(x=10, y=305)
    update_existingEmail = Entry(update_window, width=22, font="Arial 14", state=DISABLED)
    update_existingEmail.place(x=250, y=305)

    Lbl7 = Label(update_window, text="Enter Existing Phone -> ", font="Arial 16").place(x=10, y=345)
    update_existingPhone = Entry(update_window, width=22, font="Arial 14", state=DISABLED)
    update_existingPhone.place(x=250, y=345)

    Rbtn1 = Radiobutton(update_window, text="Name", variable=radio, value=1, command=radio1, font="Arial 16")
    Rbtn1.place(x=0, y=35)

    Rbtn2 = Radiobutton(update_window, text="Email", variable=radio, value=2, command=radio2, font="Arial 16")
    Rbtn2.place(x=190, y=35)

    Rbtn3 = Radiobutton(update_window, text="Phone", variable=radio, value=3, command=radio3, font="Arial 16")
    Rbtn3.place(x=370, y=35)

    Rbtn4 = Radiobutton(update_window, text="By Name", variable=radio12, value=1, command=radio4, state=DISABLED,
                        font="Arial 16")
    Rbtn4.place(x=0, y=100)

    Rbtn5 = Radiobutton(update_window, text="By Email", variable=radio12, value=2, command=radio5, state=DISABLED,
                        font="Arial 16")
    Rbtn5.place(x=190, y=105)

    Rbtn6 = Radiobutton(update_window, text="By Phone", variable=radio12, value=3, command=radio6, state=DISABLED,
                        font="Arial 16")
    Rbtn6.place(x=370, y=105)

    Btn8 = Button(update_window, text="Cancel", command=exit_update_window, font="Arial 16", width=9)
    Btn8.place(x=370, y=385)

    Btn9 = Button(update_window, text="Update Data", command=confirm_update, font="Arial 16", width=12)
    Btn9.place(x=208, y=385)

    Btn10 = Button(update_window, text="Back To Menu", command=onclick_update, font="Arial 16", width=12)
    Btn10.place(x=47, y=385)

    update_window.mainloop()

def delete_gui():
    global delete_existingName,delete_existingEmail,delete_existingPhone
    global Rbtn7, Rbtn8, Rbtn9
    global radio13
    global delete_window

    delete_window = Tk()
    delete_window.title("Deleting Data")
    delete_window.geometry("500x258")
    radio13 = IntVar()

    Lbl1 = Label(delete_window, text="Please Select Deletion Option", font="Arial 16")
    Lbl1.pack()

    Lbl2 = Label(delete_window, text="Enter Existing Name -> ", font="Arial 16").place(x=10, y=80)
    delete_existingName = Entry(delete_window, width=22, font="Arial 14", state=DISABLED)
    delete_existingName.place(x=250, y=80)

    Lbl3 = Label(delete_window, text="Enter Existing Email -> ", font="Arial 16").place(x=10, y=120)
    delete_existingEmail = Entry(delete_window, width=22, font="Arial 14", state=DISABLED)
    delete_existingEmail.place(x=250, y=120)

    Lbl4 = Label(delete_window, text="Enter Existing Phone -> ", font="Arial 16").place(x=10, y=160)
    delete_existingPhone = Entry(delete_window, width=22, font="Arial 14", state=DISABLED)
    delete_existingPhone.place(x=250, y=160)

    Rbtn7 = Radiobutton(delete_window, text="By Name", variable=radio13, value=1, font="Arial 16", command=radio7)
    Rbtn7.place(x=0, y=40)

    Rbtn8 = Radiobutton(delete_window, text="By Email", variable=radio13, value=2, font="Arial 16", command=radio8)
    Rbtn8.place(x=190, y=40)

    Rbtn9 = Radiobutton(delete_window, text="By Phone", variable=radio13, value=3, font="Arial 16", command=radio9)
    Rbtn9.place(x=370, y=40)

    Btn11 = Button(delete_window, text="Cancel", command=exit_delete_window, font="Arial 16", width=9)
    Btn11.place(x=370, y=200)

    Btn12 = Button(delete_window, text="Delete", command=confirm_delete, font="Arial 16", width=9)
    Btn12.place(x=245, y=200)

    Btn13 = Button(delete_window, text="Back To Menu", command=onclick_delete, font="Arial 16", width=12)
    Btn13.place(x=85, y=200)

    delete_window.mainloop()

def view_gui():
    global tree_name, tree_email, tree_phone, tree_city, tree_state
    global view_window
    view_window = Tk()
    view_window.title("Viewing Data")
    view_window.geometry("1025x300")

    tree_name = ttk.Treeview(view_window)
    tree_name.place(x=10, y=10)
    tree_name.heading('#0', text="Customer Name")

    tree_email = ttk.Treeview(view_window)
    tree_email.place(x=210, y=10)
    tree_email.heading('#0', text="Customer Email")

    tree_phone = ttk.Treeview(view_window)
    tree_phone.place(x=410, y=10)
    tree_phone.heading('#0', text="Phone")

    tree_city = ttk.Treeview(view_window)
    tree_city.place(x=610, y=10)
    tree_city.heading('#0', text="City")

    tree_state = ttk.Treeview(view_window)
    tree_state.place(x=810, y=10)
    tree_state.heading('#0', text="State")

    btn14 = Button(view_window, text="Cancel", command=exit_view_window, font="Arial 16", width=9)
    btn14.place(x=890, y=250)

    btn15 = Button(view_window, text="Show Records", command=viewing_records, font="Arial 16",width=12)
    btn15.place(x=728, y=250)

    btn16 = Button(view_window, text="Back To Menu", command=onclick_view, font="Arial 16",width=12)
    btn16.place(x=562, y=250)

    view_window.mainloop()

def add():
    customer_name = entryName.get()
    customer_email = entryEmail.get()
    phone = entryPhone.get()
    city = entryCity.get()
    state = entryState.get()

    print(customer_name, customer_email, phone, city, state)

    insert = "insert into customer_details values(null, '{}', '{}', '{}', '{}', '{}')".format(customer_name,
                                                                                              customer_email, phone,
                                                                                              city, state)
    con = mysql.connector.connect(user="root", password="", host="localhost", database="database_project")

    cursor = con.cursor()
    cursor.execute(insert)

    con.commit()
    messagebox.showinfo("Message", "Data has been Added Successfully")
def confirm_update():
    radiobutton = radio.get()
    radiobutton1 = radio12.get()

    if radiobutton == 1:
        if radiobutton1 == 2:
            try:
                customer_name = newName.get()
                customer_email = update_existingEmail.get()
                update1 = "update customer_details set customer_name = '{}' where customer_email = '{}'".format(
                    customer_name, customer_email)
                con = mysql.connector.connect(user="root", password="", host="localhost", database="database_project")
                cursor = con.cursor()
                cursor.execute(update1)
                con.commit()
                messagebox.showinfo("Message", "Data has been Updated Successfully")
            except:
                messagebox.showerror("ERROR","YOU HAVE NOT FILLED ANY FIELD")

        elif radiobutton1 == 3:
            try:
                customer_name = newName.get()
                phone = update_existingPhone.get()
                update2 = "update customer_details set customer_name = '{}' where phone = '{}'".format(customer_name,
                                                                                                       phone)
                con = mysql.connector.connect(user="root", password="", host="localhost", database="database_project")
                cursor = con.cursor()
                cursor.execute(update2)
                con.commit()
                messagebox.showinfo("Message", "Data has been Updated Successfully")
            except:
                messagebox.showerror("ERROR","YOU HAVE NOT FILLED ANY FIELD")
        else:
            messagebox.showerror("Error", "Please Select All option which is required for updation ")

    elif radiobutton == 2:
        if radiobutton1 == 1:
            try:
                customer_email = newEmail.get()
                customer_name = update_existingName.get()
                update3 = "update customer_details set customer_email = '{}' where customer_name = '{}'".format(
                    customer_email, customer_name)
                con = mysql.connector.connect(user="root", password="", host="localhost", database="database_project")
                cursor = con.cursor()
                cursor.execute(update3)
                con.commit()
                messagebox.showinfo("Message", "Data has been Updated Successfully")
            except:
                messagebox.showerror("ERROR","YOU HAVE NOT FILLED ANY FIELD")

        elif radiobutton1 == 3:
            try:
                customer_email = newEmail.get()
                phone = update_existingPhone.get()
                update4 = "update customer_details set customer_email = '{}' where phone = '{}'".format(customer_email,
                                                                                                        phone)
                con = mysql.connector.connect(user="root", password="", host="localhost", database="database_project")
                cursor = con.cursor()
                cursor.execute(update4)
                con.commit()
                messagebox.showinfo("Message", "Data has been Updated Successfully")
            except:
                messagebox.showerror("ERROR","YOU HAVE NOT FILLED ANY FIELD")

        else:
            messagebox.showerror("Error", "Please Select All option which is required for updation ")

    elif radiobutton == 3:
        if radiobutton1 == 1:
            try:
                phone = newPhone.get()
                customer_name = update_existingName.get()
                update5 = "update customer_details set phone = '{}' where customer_name = '{}'".format(phone,
                                                                                                       customer_name)
                con = mysql.connector.connect(user="root", password="", host="localhost", database="database_project")
                cursor = con.cursor()
                cursor.execute(update5)
                con.commit()
                messagebox.showinfo("Message", "Data has been Updated Successfully")
            except:
                messagebox.showerror("ERROR","YOU HAVE NOT FILLED ANY FIELD")

        elif radiobutton1 == 2:
            try:
                phone = newPhone.get()
                customer_email = update_existingEmail.get()
                update5 = "update customer_details set phone = '{}' where customer_email = '{}'".format(phone,
                                                                                                        customer_email)
                con = mysql.connector.connect(user="root", password="", host="localhost", database="database_project")
                cursor = con.cursor()
                cursor.execute(update5)
                con.commit()
                messagebox.showinfo("Message", "Data has been Updated Successfully")
            except:
                messagebox.showerror("ERROR","YOU HAVE NOT FILLED ANY FIELD")
        else:
            messagebox.showerror("Error", "Please Select All option which is required for updation ")
    else:
        messagebox.showerror("Error", "Please Select Any Option For Updation")

def confirm_delete():
    radiobutton = radio13.get()

    if radiobutton == 1:
        try:
            customer_name = delete_existingName.get()
            delete1 = "delete from customer_details where customer_name = '{}'".format(customer_name)
            con = mysql.connector.connect(user="root", password="", host="localhost", database="database_project")
            cursor = con.cursor()
            cursor.execute(delete1)
            con.commit()
            messagebox.showinfo("Message", "Data has been Deleted Successfully")
        except:
            messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")

    elif radiobutton == 2:
        try:
            customer_email = delete_existingEmail.get()
            delete2 = "delete from customer_details where customer_email = '{}'".format(customer_email)
            con = mysql.connector.connect(user="root", password="", host="localhost", database="database_project")
            cursor = con.cursor()
            cursor.execute(delete2)
            con.commit()
            messagebox.showinfo("Message", "Data has been Deleted Successfully")
        except:
            messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")

    elif radiobutton == 3:
        try:
            phone = delete_existingPhone.get()
            delete3 = "delete from customer_details where phone = '{}'".format(phone)
            con = mysql.connector.connect(user="root", password="", host="localhost", database="database_project")
            cursor = con.cursor()
            cursor.execute(delete3)
            con.commit()
            messagebox.showinfo("Message", "Data has been Deleted Successfully")
        except:
            messagebox.showerror("ERROR", "YOU HAVE NOT FILLED ANY FIELD")
    else:
        messagebox.showerror("Error", "Please Select Any Option For Deletion")

def viewing_records():
    global query, records
    query = "select * from customer_details"
    conn = mysql.connector.connect(user="root", password="", host="localhost", database="database_project")

    cursor = conn.cursor()
    query_result = cursor.execute(query)
    records = cursor.fetchall()
    conn.commit()
    for element in records:
        tree_name.insert('',0, text=element[1], values=element[1])
        tree_email.insert('', 0, text=element[2], values=element[2])
        tree_phone.insert('', 0, text=element[3], values=element[3])
        tree_city.insert('', 0, text=element[4], values=element[4])
        tree_state.insert('', 0, text=element[5], values=element[5])

def radio1():
    newName.configure(state="normal")
    newEmail.configure(state="disabled")
    newPhone.configure(state="disabled")
    Rbtn4.configure(state="disabled")
    Rbtn5.configure(state="normal")
    Rbtn6.configure(state="normal")

def radio2():
    newEmail.configure(state="normal")
    newPhone.configure(state="disabled")
    newName.configure(state="disabled")
    Rbtn4.configure(state="normal")
    Rbtn5.configure(state="disabled")
    Rbtn6.configure(state="normal")

def radio3():
    newEmail.configure(state="disabled")
    newPhone.configure(state="normal")
    newName.configure(state="disabled")
    Rbtn4.configure(state="normal")
    Rbtn5.configure(state="normal")
    Rbtn6.configure(state="disabled")

def radio4():
    update_existingName.configure(state="normal")
    update_existingEmail.configure(state="disabled")
    update_existingPhone.configure(state="disabled")

def radio5():
    update_existingName.configure(state="disabled")
    update_existingEmail.configure(state="normal")
    update_existingPhone.configure(state="disabled")

def radio6():
    update_existingName.configure(state="disabled")
    update_existingEmail.configure(state="disabled")
    update_existingPhone.configure(state="normal")

def radio7():
    delete_existingName.configure(state="normal")
    delete_existingEmail.configure(state="disabled")
    delete_existingPhone.configure(state="disabled")

def radio8():
    delete_existingEmail.configure(state="normal")
    delete_existingPhone.configure(state="disabled")
    delete_existingName.configure(state="disabled")

def radio9():
    delete_existingEmail.configure(state="disabled")
    delete_existingPhone.configure(state="normal")
    delete_existingName.configure(state="disabled")

def onclick_main_add():
    window.destroy()
    add_gui()

def onclick_main_update():
    window.destroy()
    update_gui()

def onclick_main_delete():
    window.destroy()
    delete_gui()

def onclick_main_view():
    window.destroy()
    view_gui()

def onclick_insert():
    add_window.destroy()
    main_gui()

def onclick_update():
    update_window.destroy()
    main_gui()

def onclick_delete():
    delete_window.destroy()
    main_gui()

def onclick_view():
    view_window.destroy()
    main_gui()

def exit_add_window():
    a = messagebox.askyesno("CONFIRM","ARE YOU SURE TO EXIT THIS PROGRAM")
    if a==1:
        add_window.destroy()

def exit_update_window():
    a = messagebox.askyesno("CONFIRM", "ARE YOU SURE TO EXIT THIS PROGRAM")
    if a == 1:
        update_window.destroy()

def exit_delete_window():
    a = messagebox.askyesno("CONFIRM", "ARE YOU SURE TO EXIT THIS PROGRAM")
    if a == 1:
        delete_window.destroy()

def exit_view_window():
    a = messagebox.askyesno("CONFIRM", "ARE YOU SURE TO EXIT THIS PROGRAM")
    if a == 1:
        view_window.destroy()

def exit_main_window():
    a = messagebox.askyesno("CONFIRM", "ARE YOU SURE TO EXIT THIS PROGRAM")
    if a == 1:
        window.destroy()

main_gui()