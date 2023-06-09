from os import stat
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#from conexion import DAO

class Ventana(Frame):
    #dao=DAO()
    def __init__(self,master=None):
        super().__init__(master,width=1000,height=400)
        self.master=master
        self.pack()
        self.crear_widgets()
    
    def crear_widgets(self):
        frame1= Frame(self,bg="#3F99F3")
        frame1.place(x=0,y=0,width=120,height=450)

        self.btnnuevo= Button(frame1,text="Alta Estudiante",command=self.fNuevo,bg="black",fg="white")
        self.btnnuevo.place(x=15,y=50,width=120,height=40)
        
        self.btnnuevo= Button(frame1,text="Actualizar Estudiante",command=self.fNuevo,bg="black",fg="white")
        self.btnnuevo.place(x=15,y=50,width=120,height=40)
