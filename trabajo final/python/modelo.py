import mysql.connector
from mysql.connector import Error 



class Conector():

    
    def _init_(self) -> Home:

        try:

            Self.conexion= mysql.connector.connect(
             host='localhost',
             port= 3306,
             user='root',
             pasword='contraseña BBDD',
             db='MiBaseDeDatos',
                 )

        except mysql.ConnectionError as descripcionErro:
            print("¡No se conecto!")

#PRIMERA OPERACION DEL CRUD: COPY 

    def InsertarValor(self, nombre, apellido, telefono,direccion):
        if self.conexion.isconnected():
            try:
                cursor=self.conexion.cursor()
                sentenciaSQL="INSERT INTO tabla de ejemplo(%s,%s,%s,%s)"
                datos=(nombre,apellido ,telefono,direccion)

                cursor.execute(sentenciaSQL,datos)
                self.conexion.commit()
                self.conexion.close()
                
            except:
                 print("No se pudo conectar a la base de datos")

#SEGUNDA OPERACION DEL CRUD : READ O LEER

    def BuscarObjeto(self, nombre):
        
        if self.conexion.is_connected ():
            try:
                cursor=self.conexion.cursor()
                sentenciaSQL= "SELECT * from tabla de ejemplo where nombre like '%mar%'"
                cursor.excute( sentenciaSQL)
                resultadoREAD= cursor.fetchall()
                self.conexion.close()
                return resultadoREAD

            except:
                print("No se pudo conectar a la base datos")

#TERCERA OPERACION DEL CRUD : UP DATE O ACTUALIZAR

    def InsertarValor(self, nombre, apellido, telefono,direccion):
        if self.conexion.isconnected():
            try:
                cursor=self.conexion.cursor()
                sentenciaSQL="UP DATE tabla de ejemplo(%s,%s,%s,%s)"
                datos=(nombre,apellido, telefono,direccion)

                cursor.execute(sentenciaSQL,datos)
                self.conexion.commit()
                self.conexion.close()
                
            except:
                 print("No se pudo conectar a la base de datos")


    


#CUARTA OPERACION DEL CRUD : DELETE O ELIMINAR

    def EliminarObjeto (self, ID):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                sentenciaSQL= "DELETE from tabla de ejemplo where id=ID"
                cursor.execute(sentenciaSQL)
                self.conexion.commit()
                self.conexion.close()

            except:
                print ("No se pudo encontrar la base dde datos")



