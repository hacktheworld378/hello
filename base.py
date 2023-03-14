from tkinter import *
from tkinter import messagebox
import PIL
import re
from PIL import Image
import sqlite3
import tkinter as tk
from db import *


mydb = MyDB("settings.db")
print(mydb.get_setting("record"))


#reset values
def clear():
    if name.get() == "" and dob == "" and age == "" and height == ""and weight == ""and bloodPressure == "" and medication == ""and pid == ""and gender == "":
        messagebox.showerror("Error", "Empty feild")
    else:
        name.set("")
        pid.set("")
        dob.set("")
        age.set("")
        height.set("")
        weight.set("")
        bloodPressure.set("")
        medication.set("")
        messagebox.showinfo("information","Date clear successfully!")
        

#Callback function
def checkname(name):
    if name.isalnum():
        return True
    if name == "":
        return True           
    else:
        messagebox.showwarning("Invalid", "Not Allowed" + name[-1])
        # return false


def submit():
    name1 = name.get()
    pid1 = pid.get()
    if len(pid1) == 0:
        msg = "Please Enter PID"
        messagebox.showinfo('message', msg)
    elif len(pid1) > 0:
        msg = "record Save Successfully"    
        messagebox.showinfo('message', msg)
       
        gender1 = gender.get()
        dob1 = dob.get()
        age1 = age.get()
        height1 = height.get()
        weight1 = weight.get()
        bloodPressure1 = bloodPressure.get()
        medication1 = medication.get()
        date1 = date.get()
        print(name1)
        print(pid1)
        print(gender1)
        print(dob1)
        print(age1)
        print(bloodPressure1)
        print(medication1)
        print(date1)
        print("==================")
        mydb.update_setting("dob", dob1)
        mydb.update_setting("bp", bloodPressure1)
        mydb.update_setting("medication", medication1)
        mydb.update_setting("date", date1)
        mydb.update_setting("name", name1)
        mydb.update_setting("pid", pid1)
        mydb.update_setting("age", age1)
        mydb.update_setting("gender", gender1)
        print("Record inserted")
        win.destroy()
#GUI
win = Tk()
win.geometry("400x400")
win.title("")
win["bg"] = "#0b0b24"
win.wm_attributes("-topmost", 1)

#create data selection variable on gui
name = StringVar()
pid = StringVar()
gender = IntVar()
dob = StringVar()
age = StringVar()
height = StringVar()
weight = StringVar()
bloodPressure = StringVar()
medication = StringVar()
date = StringVar()

checkbox1 = IntVar()
checkbox2 = IntVar()
checkbox3 = IntVar()

pos_y = 50
pos_x = 200
gap = 30
#Form Title
l = label_title = Label(win, text="Patient Details", bg="Magenta", fg="white", width=20, font=("bold", 20))
l.place(x=20, y=10)

#create fields
label_name = Label(win, text="Name:",anchor="e",bg="#0b0b24",fg="white", width=20,).place(x=5, y=pos_y)
entry_name = Entry(win, width=17, textvariable=name)
entry_name.place(x=220, y=pos_y)
validate_name = win.register(checkname)  # callback
entry_name.config(validate = "key",validatecommand =(validate_name,"%P"))#bind
pos_y = pos_y


label_pid = Label(win, text="PID:",anchor="e",bg="#0b0b24",fg="white", width=20).place(x=5, y=pos_y+gap)
entry_name = Entry(win, width=17, textvariable=pid)
entry_name.place(x=220, y=pos_y+gap)
pos_y = pos_y + gap


label_dob = Label(win, text="DOB:",anchor="e",bg="#0b0b24",fg="white", width=20).place(x=5, y=pos_y+gap)
entry_name = Entry(win, width=17, textvariable=dob)
entry_name.place(x=220, y=pos_y+gap)
pos_y = pos_y + gap


label_age = Label(win, text="Age:",anchor="e",bg="#0b0b24",fg="white", width=20).place(x=5, y=pos_y+gap)
entry_name = Entry(win, width=17, textvariable=age)
entry_name.place(x=220, y=pos_y+gap)
pos_y = pos_y + gap


label_height = Label(win, text="Height:",anchor="e",bg="#0b0b24",fg="white", width=20).place(x=5, y=pos_y+gap)
entry_name = Entry(win, width=17, textvariable=height)
entry_name.place(x=220, y=pos_y+gap)
pos_y = pos_y + gap


label_weight = Label(win, text="Weight:",anchor="e",bg="#0b0b24",fg="white", width=20).place(x=5, y=pos_y+gap)
entry_name = Entry(win, width=17, textvariable=weight)
entry_name.place(x=220, y=pos_y+gap)

pos_y = pos_y + gap


label_bloodPressure = Label(win, text="BloodPressure:",anchor="e",bg="#0b0b24",fg="white", width=20).place(x=5, y=pos_y+gap)
entry_name = Entry(win, width=17, textvariable=bloodPressure)
entry_name.place(x=220, y=pos_y+gap)
pos_y = pos_y + gap


label_medication = Label(win, text="Medication:",anchor="e",bg="#0b0b24",fg="white", width=20).place(x=5, y=pos_y+gap)
entry_name = Entry(win, width=17, textvariable=medication)
entry_name.place(x=220, y=pos_y+gap)
pos_y = pos_y + gap


label_date = Label(win, text="Date:",anchor="e",bg="#0b0b24",fg="white", width=20,).place(x=5, y=pos_y+gap)
entry_name = Entry(win, width=17, textvariable=date)
entry_name.place(x=220, y=pos_y+gap)
pos_y = pos_y + gap


label_gender = Label(win, text="Gender:", anchor="e",bg="#0b0b24", fg="white", width=20, font=("bold", 10)).place(x=5, y=pos_y + gap)
gender = StringVar()
g1_radio_male = Radiobutton(win, text="Male", padx=3, bg="white", fg="Black", variable=gender, value="Male").place(x=218, y=pos_y + gap)
# g1_radio_male.select()
g2_radio_female = Radiobutton(win,text="FeMale",padx=2,bg="white",fg="Black",variable=gender,value="Female").place(x=285,y=pos_y+gap)
# g2_radio_female.deselect()

pos_y = pos_y + gap

btn=Button(win,text='Clear Data',width=9,bg='Yellow',fg='Black',command = clear).place(x=20,y=pos_y+gap)
submitbtn=Button(win, text='Submit', width=9, bg='DarkTurquoise', fg='Black', command = submit).place(x=140, y=pos_y + gap)
exitButton=Button(win,text='Close',width=9,bg='Magenta',fg='Black',command = win.destroy).place(x=265,y=pos_y+gap)
pos_y = pos_y + gap


win.mainloop()
