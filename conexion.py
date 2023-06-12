import sqlite3
import _sqllite3

class DAO:
    def __init__(self):
        try:
            self.con=sqlite3.connect("estudiantes.db")
            cursor=self.con.cursor()
            print("Conectado correctamente")
            
        except:
            print("Error de conexion")
    def __str__(self): #funcion magicva que imprime todo lo que tiene el constructor
        datos=self.consulta_estudiantes()
        aux=""
        for row in datos:
            aux=aux + str(row)+"\n"
        return aux
    
    def consulta_estudiantes(self):
        cur=self.con.cursor()
        cur.execute("SELECT * FROM Estudiante")
        datos=cur.fetchall()
        cur.close()
        return datos
    
    def eliminar_estudiante(self,codigo):
        cur=self.con.cursor()
        sql="""DELETE FROM Estudiante WHERE idEstudiante={}""",format(codigo)
        cur.execute(sql)
        n=cur.rowcount
        self.con.commit()
        cur.close()
        return n