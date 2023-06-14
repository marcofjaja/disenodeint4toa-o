from tkinter import *
from tkinter import ttk
from ventana import *

def main():
    root = Tk()

    root.wm_title("Crud tkinter y Mysql")
    app = Ventana(root)
    app = mainloop()

if __name__== "__main__":
    main()