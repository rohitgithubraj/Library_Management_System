from tkinter import *
from tkinter import messagebox import sqlite3
from sqlite3 import Error
from datetime import datetime,date import os
import sys
py = sys.executable
 

class renew(Tk): def  init (self):
super(). init () self.iconbitmap(r'libico.ico') self.configure(bg='tan2') self.title("Renew") self.maxsize(600,400) self.minsize(600, 400)
a = StringVar()
b = StringVar() self.cal = 0

def days_between(d1, d2):
d1 = datetime.strptime(d1, "%Y-%m-%d") d2 = datetime.strptime(d2, "%Y-%m-%d") return abs((d2 - d1).days)

def qui():
if len(a.get()) == 0 or len(b.get()) == 0: messagebox.showerror("Error","Please Enter The Id's")
else:
try:
self.conn = sqlite3.connect('library_administration.db') self.mycursor = self.conn.cursor()
 
self.mycursor.execute("Select BID from issue where BID = ?",[a.get()]) temp = self.mycursor.fetchone()
self.mycursor.execute("Select Fine from students where Student_Id = ?",
[b.get()])
fine = self.mycursor.fetchone()
self.mycursor.execute("Select Return_date from issue where BID = ? and SID = ?", [a.get(), b.get()])
temp1 = self.mycursor.fetchone() if temp1:
da = str(date.today()) ea = str(temp1[0])
if da < ea:
messagebox.showinfo("Oops", "Your Return Date Has not yet come") else:
self.cal = days_between(ea, da) self.cal += int(fine[0])
if int(self.cal) >= 100:
messagebox.showinfo("Fine", "Your Id is banned.Please pay the
fine")
elif int(self.cal) > 0:
messagebox.showinfo('Warning','Please Return/Renew book Timely to avoid termination of id')
self.mycursor.execute("Update students set Fine = ? where Student_Id = ?",[int(self.cal), b.get()])
self.mycursor.execute("UPDATE issue set Issue_date = date('now') where BID =? ", [a.get()])
self.mycursor.execute("update issue set Return_date = date('now','+15 days') where BID = ?",[a.get()])
self.conn.commit()
 
self.conn.close()
messagebox.showinfo('Info', 'Succesfully Renewed')
c = messagebox.askyesno("Confirm", "Do you want to renew another
book?")
if c:
self.destroy()
os.system('%s %s' % (py, 'renew.py')) else:
self.destroy()
else:
messagebox.showinfo("Oop's", "The Book is not yet issued") except TypeError:
messagebox.showerror("Error", "Check The Texts") except Error:
messagebox.showerror("Error","Check The Fields")

Label(self, text='Renew Book', font=('Algerian', 35, 'bold'),bg="tan2").pack() Label(self, text='Enter Book ID',font=('Comic Scan Ms', 15, 'bold'),
bg="tan2").place(x=80, y=150)
Entry(self, textvariable=a, width=40).place(x=280, y=150) Label(self, text="Enter Student Id",font=('Comic Scan Ms', 15,
'bold'),bg="tan2").place(x=80, y=200)
Entry(self, textvariable=b, width=40).place(x=280, y=200) Button(self, text="Renew", width=25, command=qui,
background="burlywood3",font=('Arial', 10, 'bold')).place(x=280, y=300)


renew().mainloop()
