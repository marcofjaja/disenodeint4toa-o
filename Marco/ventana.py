from decimal import FloatOperation
from os import stat#importamos sistema operativo
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conexion import DAO#importamos el archivo de conexion

class Ventana(Frame):
    dao=DAO()#instanciamos dao de la clase principal DAO del archivo conexion.py
    def __init__(self,master=None):
        super().__init__(master,width=1000,height=400)
        self.master=master
        self.pack()
        self.crear_widgets()#creamos todos los controles
        self.cargarDatos()#los datos que trae esta funcion d ela base de datos
        self.habilitarTexto("normal")#activado normal- disabled lo deshabilita
        self.habilitarBotonesEventos("normal")
        self.habilitarBotonesGuardar("normal")
        self.limpiarTexto()
        self.bandera="Guardar"

    #Todas las funciones del crud y Botones, Eventos, etc  
    #cargar Datos en el grid
    def cargarDatos(self):
        datos=self.dao.consulta_estudiantes()#del objeto dao traeme la consulta_estudiante que trae todos los elementos de la base de datos
        for row in datos:#los datos traidos de la base de datos los pone en row
            self.grid.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4],row[5],row[6]))
            # row[0]es el codigo,                        nombre  altura peso sexo    indice de masa corporal
            
    def habilitarTexto(self,estado):
        self.txtCodigo.configure(state=estado)#caja de textoESTADO ACTIVO normal O DESACTIVADO disabled
        self.txtNombre.configure(state=estado)
        self.txtAltura.configure(state=estado)
        self.txtPeso.configure(state=estado)
        self.txtSexo.configure(state=estado)

    def habilitarBotonesEventos(self,estado):
        self.btnNuevo.configure(state=estado)# botones eventos ESTADO ACTIVO normal O DESACTIVADO disabled
        self.btnActualizar.configure(state=estado)
        self.btnEliminar.configure(state=estado)
      
    def habilitarBotonesGuardar(self,estado):
        self.btnGuardar.configure(state=estado)# botones eventos ESTADO ACTIVO normal O DESACTIVADO disabled
        self.btnCancelar.configure(state=estado)
                
    def limpiarTexto(self):
        self.txtCodigo.delete(0,END)# LLE ESTA DICIENDO LA linea que tiene delete mandala al final y limpiala
        self.txtNombre.delete(0,END) 
        self.txtAltura.delete(0,END)   
        self.txtPeso.delete(0,END)    
        self.txtSexo.delete(0,END)  
        self.txtCodigo.focus()#pone el foco en la caja de texto codigo
        
    def limpiarGrid(self):
        for item in self.grid.get_children():#obtengo todos los datos del grid
            self.grid.delete(item)# recorre todos los registos item x item y le dice que los borre a todos
            
    def fNuevo(self):
        self.habilitarTexto("normal")
        self.habilitarBotonesEventos("disabled")
        self.habilitarBotonesGuardar("normal")
        self.limpiarTexto()
        
    def fActualizar(self):
        select=self.grid.focus()#selecciona el id
        #print(select)
        row=self.grid.item(select)#todos los campos cdel registro con ese id
        #print(row)   
        codigo=self.grid.item(select,"text")
        #print(codigo)
        valores=self.grid.item(select,"values")
        print(valores)
        if codigo=="":#si codigo=a vacio
           messagebox.showwarning("Modificar","Debes seleccionar un elemento para poder modificar") 
        else:
            #cambiar el self.codigo por el valor del codigo
            self.bandera="Actualizar"#cambia la bandera de Guardar a Actualizar MUY IMPORTANTE PARA PODER ACTUALIZAR NO GUARDAR
            print(f"Mostrando el estado de la bandera: {self.bandera}") 
            print(valores)
            self.habilitarTexto("normal")  
            self.limpiarTexto()
            self.habilitarBotonesGuardar("normal")
            self.txtCodigo.insert(0,codigo)#LE DECIMOS QUE INSERTE EN LAS CAJAS DE TEXTO LOS VALORES QUE TENGO SELECCIONADOS
            self.txtNombre.insert(0,valores[0])
            self.txtAltura.insert(0,valores[1])
            self.txtPeso.insert(0,valores[2])
            self.txtSexo.insert(0,valores[3])
            
            
        
    def fEliminar(self):
        select=self.grid.focus() #selecciona el id
       # print(select)     
        row=self.grid.item(select) #todos los campos de ese rgistro (fila)
      #  print(row)
        codigo=self.grid.item(select,"text")#selecciona el codico de row
        #print(codigo)
        valores=self.grid.item(select,"values")#guarda todos los valores del registo con ese codigo
        #print(valores)
        if codigo=="":#si el codigo esta vacio envia un mensaje
            messagebox.showwarning("Eliminar","Debes seleccionar un elemento")
        else:
            r=messagebox.askquestion(f"Eliminar","Estas seguro de eliminarlo?")#Guardo la respuesta a la pregunta de un cuadro de texto
            if r==messagebox.YES:#condiciono la variable r (yes o not) si es YES
                n=self.dao.eliminar_estudiante(codigo)#LLAMA A funcio dao en conexion a eliminar_estudiante que espera le pase un código que aqui lo tengo como argumento y lo recibira como parametro
                if n==1:#si es igual a 1 mostra el siguiente mensaje
                    messagebox.showinfo("Eliminar","Registro eliminado correctamente")
                    self.limpiarGrid()  #LIMPI EL GRID
                    self.cargarDatos()#CARGO LOS datos
                else:#sino es igual a uno muestro este otro mensaje
                    messagebox.showinfo("Eliminar","No se pudeo elimiar el registro")
            else:
                pass        
    def fGuardar(self):
        if self.bandera == "Guardar":
           cod=self.txtCodigo.get()#OBTENGO EL TEXTO DE LA CAJA
           nom=self.txtNombre.get()
           al=self.txtAltura.get()
           pe=self.txtPeso.get()
           se=self.txtSexo.get()
           imc2023=(float(pe)/(float(al)*(float(al))))
           imc2024=0
           try:
              self.dao.inserta_estudiante(cod,nom,al,pe,se,imc2023,imc2024)  
              messagebox.showinfo("Guardar","Registro Guardado Exitosamente")
              self.limpiarGrid()
              self.cargarDatos()
              self.limpiarTexto()
              self.habilitarBotonesGuardar("disabled")
              self.habilitarBotonesEventos("normal")
              self.habilitarTexto("disabled")
           except:
              messagebox.showinfo("Guardar","No se pudo guardar el registro")
        elif self.bandera=="Actualizar":
          #  messagebox.showinfo("Modificar","Modifico")
            cod=self.txtCodigo.get()#OBTENGO EL TEXTO DE LA CAJA
            nom=self.txtNombre.get()
            al=self.txtAltura.get()
            pe=self.txtPeso.get()
            se=self.txtSexo.get()
            imc2023=(float(pe)/(float(al)*(float(al))))
            imc2024=0
            self.dao.modificar_estudiantes(nom,al,pe,se,imc2023,imc2024,cod)  
            messagebox.showinfo("Actualizar","Registro Modificado Exitosamente")
            #MUY IMPORTANTE REGRESAR EL ESTADO A GUARDAR
            self.bandera="Guardar"
            self.limpiarGrid()
            self.cargarDatos()
            self.limpiarTexto()
            self.habilitarBotonesGuardar("disabled")
            self.habilitarBotonesEventos("normal")
            self.habilitarTexto("disabled")
          #except:
              #   messagebox.showinfo("Actualizar","No se pudo Actualizar el registro")
                
             
    def fCancelar(self):
        self.limpiarGrid()
        self.cargarDatos()
        self.limpiarTexto()
        self.habilitarBotonesGuardar("disabled")
        self.habilitarBotonesEventos("normal")
        self.habilitarTexto("disabled")     
             
    def crear_widgets(self):
       #imprimir cuadro a la izq
       frame1=Frame(self,bg="#3F99F3")
       frame1.place(x=0,y=0,width=1200,height=700)#con x que Quede pegado al lado izq y de y pegado al borde superior
       #Boton nuevo
                           #posicionado dentro del frame1 con un texto Nuevo Estudiante
       self.btnNuevo=Button(frame1,text="Alta Estudiante", command=self.fNuevo,bg="black", fg="white")
       self.btnNuevo.place(x=15,y=50,width=120, height=40)
       
       #Boton actualizar estudiante
       self.btnActualizar=Button(frame1,text="Actualizar Estudiante", command=self.fActualizar,bg="black", fg="white")
       self.btnActualizar.place(x=15,y=140,width=120, height=40)
       
         #Boton eliminar estudiante
       self.btnEliminar=Button(frame1,text="Eliminar Estudiante", command=self.fEliminar,bg="black", fg="white")
       self.btnEliminar.place(x=15,y=220,width=120, height=40)
       
       #seccion de datos
       frame2=Frame(self,bg="#5DADE2")
       frame2.place(x=150,y=0,width=1200,height=900)
       
       #Primera etiqueta de código o idEstudiante
       lbl1=Label(frame2,text="Código: ")
       lbl1.place(x=30, y=30)
       self.txtCodigo=Entry(frame2)
       self.txtCodigo.place(x=30,y=58,width=150,height=20)
       
        #Segunda etiqueta de Nombre
       lbl2=Label(frame2,text="Nombre y Apellido: ")
       lbl2.place(x=30, y=95)
       self.txtNombre=Entry(frame2)
       self.txtNombre.place(x=30,y=125,width=150,height=20)
       
           #Tercera etiqueta de altura
       lbl3=Label(frame2,text="Altura: ")
       lbl3.place(x=30, y=160)
       self.txtAltura=Entry(frame2)
       self.txtAltura.place(x=30,y=190,width=150,height=20)
       
           #Cuarta etiqueta de peso
       lbl4=Label(frame2,text="Peso: ")
       lbl4.place(x=30, y=220)
       self.txtPeso=Entry(frame2)
       self.txtPeso.place(x=30,y=250,width=150,height=20)
       
           #quinta  etiqueta de sexo
       lbl5=Label(frame2,text="Sexo: ")
       lbl5.place(x=30, y=275)
       self.txtSexo=Entry(frame2)
       self.txtSexo.place(x=30,y=305,width=150,height=20)
       
       
       #Botones de guardado
       #Boton guardar
       self.btnGuardar=Button(frame2,text="Guarda",command=self.fGuardar,bg="#0B4162",fg="white") 
       self.btnGuardar.place(x=20,y=340,width=90,height=40)
       
       #Boton Cancelar
       self.btnCancelar=Button(frame2,text="Cancelar",command=self.fCancelar,bg="#EC7063",fg="white") 
       self.btnCancelar.place(x=120,y=340,width=90,height=40)
       
       #GRID sistema de grillas donde vamos a mostrar los datos
       frame3=Frame(self,bg="#D6EAF8")
       frame3.place(x=380,y=0,width=1000,height=750)
       
       self.grid=ttk.Treeview(self,columns=("col1","col2","col3","col4","col5","col6","col7"))
       
       self.grid.column("#0",width=50,anchor=CENTER)#CAMPO CERO VA A SER EL ID
       self.grid.column("col1",width=140,anchor=CENTER)#anchor le estamos diciendo que la vamos a centrar dentro del grid
       self.grid.column("col2",width=50,anchor=CENTER)
       self.grid.column("col3",width=50,anchor=CENTER)
       self.grid.column("col4",width=50,anchor=CENTER)
       self.grid.column("col5",width=180,anchor=CENTER)
       self.grid.column("col6",width=200,anchor=CENTER)
       self.grid.column("col7",width=200,anchor=CENTER)
       
       self.grid.heading("#0",text="Código",anchor=CENTER)#el encabezado para las columnas
       self.grid.heading("col1",text="Nombre y Apellido",anchor=CENTER)
       self.grid.heading("col2",text="Altura",anchor=CENTER)
       self.grid.heading("col3",text="Peso",anchor=CENTER)
       self.grid.heading("col4",text="Sexo",anchor=CENTER)
       self.grid.heading("col5",text="Indice de Masa Corporal 2023",anchor=CENTER)
       self.grid.heading("col6",text="Indice de Masa Corporal 2024",anchor=CENTER)
       
       #Ponerlo
       self.grid.place(x=400,y=0,width=525,height=400)
       #Seleccionar uno solo
       self.grid['selectmode']='browse'#el usuario va a poder seleccionar entre multiples estuadiantes
       
       #demo insert para probar antes de declarar las funcioens a metodos desde widgets
       #self.grid.insert("",END,text="1",values=("Juana Manso",1.56,45,"M",45/(1.56*1.56)))#al codigo lo pone con la palabra text=1 le da valor uno
       
       
       
           #Sexta  etiqueta de Indice masa corporal 2023
    """   lbl1=Label(frame2,text="Nombre: ")
       lbl1.place(x=30, y=30)
       self.txtCodigo=Entry(frame2)
       self.txtCodigo.place(x=30,y=58,width=150,height=20)
       
              #Septima  etiqueta de Indice masa corporal 2024
       lbl1=Label(frame2,text="Nombre: ")
       lbl1.place(x=30, y=30)
       self.txtCodigo=Entry(frame2)
       self.txtCodigo.place(x=30,y=58,width=150,height=20)"""