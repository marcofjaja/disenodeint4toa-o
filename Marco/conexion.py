
import sqlite3
import _sqlite3

class DAO:
    def __init__(self):
       try: 
         self.con=sqlite3.connect("estudiantes.db")
         cursor=self.con.cursor()
         print("Conectado correctamente")
         
       except:
           print("Error de conexión")  
    def __str__(self):#metodo magico str sirve para imprimir automaticamente lo que tengamso en el constructor o lo que le mandemos a hacer
        datos=self.consulta_estudiantes()
        aux=""
        for row in datos:
            aux=aux + str(row)+"\n"     
        return aux
    
    def consulta_estudiantes(self):
        cur=self.con.cursor()
        cur.execute("SELECT * FROM Estudiante")
        datos=cur.fetchall()#lo guarda en una tupla
        cur.close()     #cierra la base de datos
        return datos
    
    def eliminar_estudiante(self,codigo):
        cur=self.con.cursor()#CONECTAMOS A LA BD
        sql='''DELETE FROM Estudiante WHERE idEstudiante={}'''.format(codigo)
        cur.execute(sql)
        n=cur.rowcount#SI n==1 se borro el elemento
        self.con.commit()
        cur.close()
        return n
    
    def modificar_estudiantes(self,nombre_apellido,altura,peso,sexo,IndiceMasaCorporal2023,IndiceMasaCorporal2024):
        cur=self.con.cursor()
        sql='''UPDATE Estudiante SET nombre_apellido='{}',altura='{}',peso='{}',sexo='{}',IndiceMasaCorporal2023='{}', IndiceMasaCorporal2024='{}' WHERE codigo={}'''.format(nombre_apellido,altura,peso,sexo,IndiceMasaCorporal2023,IndiceMasaCorporal2024)
        cur.execute(sql)#ejecutame
        n=cur.rowcount#validame
        self.con.commit()#guarda en la base de datos
        
        cur.close()
        return 
    def inserta_estudiante(self,cod,nom,al,pe,se,imc2023,imc2024):
        cur=self.con.cursor()
        sql='''INSERT INTO Estudiante (idEstudiante, nombre_apellido,altura,peso,sexo,IndiceMasaCorporal2023, IndiceMasaCorporal2024) VALUES('{}','{}','{}','{}','{}','{}','{}')'''.format(cod,nom,al,pe,se,imc2023,imc2024)
        cur.execute(sql)#ejecutame
        n=cur.rowcount#validame ==1 inserto elementos
        self.con.commit()#guarda en la base de datos
        cur.close()
        return n
a=DAO()  
print(a)     

  