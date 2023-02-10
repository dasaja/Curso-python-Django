#Importar sqlite3
import sqlite3

#Conectarnos a la DB vehículos
con = sqlite3.connect("Coches.db")



#Registrar fabricantes
#register1 = (1, "Honda", "911234567", "calle Cuenca", "correo@correo.com")
#register2 = (2, 'Seat', '919287567', 'Calle Espana 1', 'info@seat.es')
register3 = (3, 'Toyota', '919287589', 'Calle Azuay', 'Dan@fun.com')
register4 = (4, 'Mazda', '934587510', 'Calle Cuba', 'padawan@fun.com')


#Insert
cursor = con.cursor()
#cursor.execute("INSERT INTO Fabricante VALUES(?,?,?,?,?)", register1)
#cursor.execute("INSERT INTO Fabricante VALUES(?,?,?,?,?)", register2)
cursor.execute("INSERT INTO Fabricante VALUES(?,?,?,?,?)", register3)
cursor.execute("INSERT INTO Fabricante VALUES(?,?,?,?,?)", register4)

#commit de operaciones
con.commit()


#Cerrar la conexión
con.close()
