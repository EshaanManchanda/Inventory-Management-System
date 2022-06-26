from tkinter import *
from tkinter import font
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk, messagebox # to import droup down list or chombo box
import sqlite3


class salesClass: #we are make class here
    def __init__(self,root):#this is defaule constructor. root is the object
        self.root = root#this define object of class using self(this is concept of oop's)
        self.root.geometry("1100x500+210+140")#it is used to define size of the frame or window
        self.root.title("Sales")
        self.root.config(bg="white")
        self.root.focus_force()
        
        self.var_invoice=StringVar()
        
        #=====Title ==========================
        lbl_title = Label(self.root,text="View Customer Bill",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        
        lbl_invoice=Label(self.root,text="Invoice No.",font=("times new roman",15),bg="white").place(x=50,y=100)
        
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",15),bg="lightyellow").place(x=160,y=100,width=180,height=28)
        
        btn_search=Button(self.root,text="Search",font=("times new roman",15,"bold"),cursor="hand2",bg="#2196f3",fg="white").place(x=360,y=100,width=120,height=28)
        
        btn_clear=Button(self.root,text="Clear",font=("times new roman",15,"bold"),cursor="hand2",bg="lightgray").place(x=490,y=100,width=120,height=28)
        
        
        
if __name__ == "__main__":
    root=Tk()#make root oject of tk class
    obj=salesClass(root)#making obj  object of IMS class, passig   root to attache with tk class
    root.mainloop()#i  use this program to stay the window  otherwise it exit imidately 