from tkinter import * from tkinter import ttk
from tkinter import messagebox import sqlite3
 
from sqlite3 import Error import os,glob



class Sst(Tk):
def  init (self): super(). init ()
f = StringVar()
g = StringVar() self.configure(bg='tan2') self.title("Search Student") self.maxsize(800,500) self.minsize(800,500) self.iconbitmap(r'libico.ico')
l1=Label(self,text="Search Student",font=("Algerian",20,'bold'), bg="tan2").place(x=290,y=20)
l = Label(self, text="Search By", font=("Arial", 15, 'bold'), bg="tan2").place(x=60, y=96)
def writeTofile(data,filename): with open(filename,'wb') as file:
file.write(data)


def insert(data): self.listTree.delete(*self.listTree.get_children()) for row in data:
self.listTree.insert("","end",text = row[2], values = (row[1],row[4],row[6]))
 
def ge():
if (len(g.get())) == 0:
messagebox.showinfo('Error', 'First select a item') elif (len(f.get())) == 0:
messagebox.showinfo('Error', 'Enter the '+g.get()) elif g.get() == 'Name':
try:
self.conn = sqlite3.connect('library_administration.db') self.mycursor = self.conn.cursor()
self.mycursor.execute("Select * from students where name like
?",['%'+f.get()+'%'])
pc = self.mycursor.fetchall() if pc:
insert(pc) else:
messagebox.showinfo("Oop's","Name not found") except Error:
messagebox.showerror("Error", "Something goes wrong") elif g.get() == 'ID':
try:
self.conn = sqlite3.connect('library_administration.db') self.mycursor = self.conn.cursor()
self.mycursor.execute("Select * from students where Student_Id like ?", ['%' + f.get() + '%'])
pc = self.mycursor.fetchall() if pc:
 
insert(pc) else:
messagebox.showinfo("Oop's", "Id not found") except Error:
messagebox.showerror("Error", "Something goes wrong")




b=Button(self,text="Find",width=15,font=("Arial",10,'bold'),command=ge, background="burlywood3").place(x=460,y=148)

c=ttk.Combobox(self,textvariable=g,values=["Name","ID"],width=40,state="readonly ").place(x = 180, y = 100)
en = Entry(self,textvariable=f,width=43).place(x=180,y=155)
la = Label(self, text="Enter", font=("Arial", 15, 'bold'), bg="tan2").place(x=100, y=150)


def handle(event):
if self.listTree.identify_region(event.x,event.y) == "separator": return "break"



self.listTree = ttk.Treeview(self, height=13,columns=('Student Name', 'Phone Number', 'No. Of Books Issued'))
self.vsb = ttk.Scrollbar(self,orient="vertical",command=self.listTree.yview) self.listTree.configure(yscrollcommand=self.vsb.set) self.listTree.heading("#0", text='Student ID', anchor='w') self.listTree.column("#0", width=100, anchor='w') self.listTree.heading("Student Name", text='Student Name')
 
self.listTree.column("Student Name", width=200, anchor='center') self.listTree.heading("Phone Number", text='Phone Number') self.listTree.column("Phone Number", width=200, anchor='center') self.listTree.heading("No. Of Books Issued", text='No. Of Books Issued') self.listTree.column("No. Of Books Issued", width=200, anchor='center') self.listTree.bind("<Button-1>", handle)
self.listTree.place(x=40, y=200) self.vsb.place(x=743,y=200,height=287) ttk.Style().configure("Treeview", font=('Times new Roman', 15))

Sst().mainloop()
