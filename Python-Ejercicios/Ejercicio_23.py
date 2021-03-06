#En este ejercicio tendréis que crear una tabla llamada Alumnos que constará de tres columnas:
# la columna id de tipo entero, la columna nombre que será de tipo texto y la columna apellido
# que también será de tipo texto.
# Una vez creada la tabla, tenéis que insertarle datos, como mínimo tenéis que insertar 8 alumnos a la tabla.
# Por último, tienes que realizar una búsqueda de un alumno por nombre y mostrar los datos por consola.

import sqlite3

db_connection = sqlite3.connect('ejercicio_25.db')
db_cursor = db_connection.cursor()

db_cursor.execute("CREATE TABLE Alumnos(Id INT, Nombre TEXT, Apellido TEXT)")

db_cursor.execute("INSERT INTO Alumnos VALUES(1,'Primero', 'Segundo')")
db_cursor.execute("INSERT INTO Alumnos VALUES(2,'Tercero', 'Cuarto')")
db_cursor.execute("INSERT INTO Alumnos VALUES(3,'Quinto', 'Sexto')")
db_cursor.execute("INSERT INTO Alumnos VALUES(4,'Septimo', 'Octavo')")
db_cursor.execute("INSERT INTO Alumnos VALUES(5,'Noveno', 'Decimo')")
db_cursor.execute("INSERT INTO Alumnos VALUES(6,'DecimoPrimero', 'DecimoSegundo')")
db_cursor.execute("INSERT INTO Alumnos VALUES(7,'DecimoTercero', 'DecimoCuarto')")
db_cursor.execute("INSERT INTO Alumnos VALUES(8,'DecimoQuinto', 'DecimoSexto')")

db_connection.commit()

db_cursor.execute("SELECT * FROM Alumnos WHERE Nombre = 'Noveno'")

filas = db_cursor.fetchall()

print(filas)

db_connection.close()