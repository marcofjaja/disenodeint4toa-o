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
    

