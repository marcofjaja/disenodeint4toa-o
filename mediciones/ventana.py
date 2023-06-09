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
        
        self.btnActualizar= Button(frame1,text="Actualizar Estudiante",command=self.fActualizar,bg="black",fg="white")
        self.btnActualizar.place(x=15,y=140,width=120,height=40)
         
        self.btnEliminar= Button(frame1,text="Eliminar Estudiante", command=self.fEliminar,bg="black",fg="white")
        self.btnEliminar.place(x=15,y=220,width=120,height=40)
        
        frame2= Frame(self,bg="#5DADE2")
        frame2.place(x=150,y=0,width=230,height=450)
        
        #Primera etiqueta codigo
        lbl1= Label(frame2,text="Còdigo: ")
        lbl1.place(x=30,y=30)
        self.txtCodigo=Entry(frame2)
        self.txtCodigo.place(x=30,y=58,width=150,height=20)
        
        #Segunda etiqueta de Nombre
        lbl2= Label(frame2,text="Nombre y Apellido: ")
        lbl2.place(x=30,y=95)
        self.txtNombre=Entry(frame2)
        self.txtNombre.place(x=30,y=125,width=150,height=20)
        
