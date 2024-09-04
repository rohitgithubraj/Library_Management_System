from tkinter import *
from tkinter import messagebox import sqlite3
from sqlite3 import Error import os
import sys
py = sys.executable


#creating window class Add(Tk):
def  init (self): super(). init ()
self.iconbitmap(r'libico.ico') self.maxsize(500, 500)
self.minsize(500, 500) self.configure(bg='tan2') self.title('Add Book')
a = StringVar()
b = StringVar()
c = StringVar() #verifying Input def b_q():
if len(a.get()) == 0 or len(b.get()) == 0: messagebox.showerror("Error","Please Enter The Details")
 
else:
g = 1 try:
self.conn = sqlite3.connect('library_administration.db')
self.myCursor = self.conn.cursor() self.myCursor.execute("Insert into books values
(?,?,?,?)",[a.get(),b.get(),c.get(),g])
self.conn.commit()
messagebox.showinfo('Info', 'Succesfully Added')
ask = messagebox.askyesno("Confirm", "Do you want to add another
book?")
if ask:
self.destroy()
os.system('%s %s' % (py, 'Add_Books.py')) else:
self.destroy() except Error:
messagebox.showerror("Error","Check The Details") #creating input box and label
Label(self, text='', background='tan2').pack()
Label(self, text='Book Details', font=('Algerian', 25, 'bold'), background='tan2').pack()
Label(self, text='', background='tan2').pack()
Label(self, text='Book Id:', font=('Comic Scan Ms', 15, 'bold'), background='tan2').place(x=100, y=130)
Entry(self, textvariable=a, width=30).place(x=250, y=132) Label(self, text='Book Name:', font=('Comic Scan Ms', 15, 'bold'),
background='tan2').place(x=100, y=180)
 
Entry(self, textvariable=b, width=30).place(x=250, y=182)
Label(self, text='Book Author:', font=('Comic Scan Ms', 15, 'bold'), background='tan2').place(x=100, y=230)
Entry(self, textvariable=c, width=30).place(x=250, y=232)
Button(self, text="Submit", font=('Comic Scan Ms', 15, 'bold'), command=b_q, background="burlywood3", padx=5).place(x=200, y=300)
Add().mainloop()
