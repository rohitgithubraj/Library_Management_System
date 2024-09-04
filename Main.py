from tkinter import *
from tkinter import messagebox import sqlite3
from sqlite3 import Error import os py=sys.executable



#creating window class Lib(Tk):
def  init (self): super(). init () self.a = StringVar() self.b = StringVar()
 
self.maxsize(1000, 400)
self.minsize(1000, 400) self.state("zoomed") self.iconbitmap(r'libico.ico')
self.canvas = Canvas(width=1100, height=500, bg='blue') self.canvas.pack()
self.photo = PhotoImage(file='770x385-UK-Library-Books.png') self.canvas.create_image(0, 0, image=self.photo, anchor=NW)










#verifying input def chex():
if len(self.user_text.get()) < 0: messagebox.showinfo("Oop's","Please Enter Your User Id")
elif len(self.pass_text.get()) < 0: messagebox.showinfo("Oop's","Please Enter Your Password")
else:
try:
self.conn = sqlite3.connect('library_administration.db') self.myCursor = self.conn.cursor()
self.myCursor.execute("Select * from admin where id=? AND password
=?",[self.user_text.get(),self.pass_text.get()])
 
self.pc = self.myCursor.fetchall() self.myCursor.close() self.conn.close()
if self.pc: self.destroy()
os.system('%s %s' % (py, 'options.py')) else:
messagebox.showinfo('Error', 'Username and password not found') self.user_text.delete(0, END)
self.pass_text.delete(0, END) except Error:
messagebox.showinfo('Error',"Something Goes Wrong,Try restarting") def fp():
os.system('%s %s' % (py, 'f_passwd.py'))


def reg():
os.system('%s %s' % (py, 'reg.py'))


def check(): try:
conn = sqlite3.connect('library_administration.db') mycursor = conn.cursor() mycursor.execute("Select * from admin")
z = mycursor.fetchone() mycursor.close() conn.close()
 
if not z:
messagebox.showinfo("Error", "Please Register A user")
x = messagebox.askyesno("Confirm","Do you want to register a user") if x:
self.destroy()
os.system('%s %s' % (py, 'Reg.py')) else:
self.label = Label(self, text="Login", anchor=W, font=("Algerian", 40, 'bold', 'underline'),bg="tan2")
self.label.place(x=450, y=10)
self.label1 = Label(self, text="User-Id", font=("Times New roman", 20, 'bold'), bg="tan2")
self.label1.place(x=310, y=100)
self.user_text = Entry(self, textvariable=self.a, width=45) self.user_text.place(x=500, y=115)
self.label2 = Label(self, text="Password", font=("Times new roman", 20, 'bold'),bg="tan2")
self.label2.place(x=310, y=150)
self.pass_text = Entry(self, show='*', textvariable=self.b, width=45) self.pass_text.place(x=500, y=165)
self.butt = Button(self, text="Login", font=10, width=15, command=chex,background="burlywood3").place(x=350, y=215)
self.butt2 = Button(self, text="Forgot Password", font=10, width=18, command=fp, background="burlywood3").place(x=530, y=215)
self.label3 = Label(self, text="Don't have an account? Register one now..", font=("Times new roman", 20, 'bold'),bg="tan2")
self.label3.place(x=285, y=270)
self.butt2 = Button(self, text="Register", font=10, width=18, command=reg, background="burlywood3").place(x=440, y=320)
 

except Error:
messagebox.showinfo("Error", "Something Goes Wrong")


check()


Lib().mainloop()
