from tkinter import * from tkinter import ttk
from tkinter import messagebox import sqlite3
from sqlite3 import Error import re
import sys,os
py = sys.executable




#creating window class Fine(Tk):
 
def  init (self): super(). init ()
self.iconbitmap(r'libico.ico') self.maxsize(500, 300)
self.minsize(500, 300) self.configure(bg='tan2') self.title("Clear Fine") #creating variables
a = StringVar() def clear():
if len(a.get()) == 0: messagebox.showerror("Error","Please Enter The Id")
elif a.get().isdigit(): try:
self.conn = sqlite3.connect('library_administration.db') self.myCursor = self.conn.cursor() self.myCursor.execute("Select Student_Id from students") student = self.myCursor.fetchall()
listStudent = list(student) if listStudent:
for sid in listStudent: if int(a.get()) in sid:
con = messagebox.askyesno("Confirm","Are You Sure you want to
clear the fine?")
if con:
self.myCursor.execute("Update students set Fine = 0 where Student_Id = ?",[a.get()])
 
self.conn.commit() self.conn.close()
messagebox.showinfo("Successful","All Fine Cleared")
d = messagebox.askyesno("Confirm","Do you want to clear
another fine?")
if d:
self.destroy()
os.system('%s %s'% (py,'fine.py')) else:
self.destroy()
else:
messagebox.showinfo("Oops","The Id you entered is not found")
else:
messagebox.showerror("Error","Please Check The Id") except:
messagebox.showinfo("Oops","Something Goes Wrong") else:
messagebox.showerror("Error","Please Check The Id")
Label(self,text="Enter Student Id", font = ('arial',15,'bold'), bg='tan2').place(x=50,y=100)
Entry(self,textvariable=a,width=40).place(x=230,y=105) Button(self, text='Clear Fine', width=20,command = clear,
background="burlywood3", font = ('arial',10,'bold')).place(x=180, y=155) Fine().mainloop()
 
