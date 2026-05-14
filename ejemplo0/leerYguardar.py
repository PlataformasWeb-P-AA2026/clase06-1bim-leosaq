"""
    Leer información desde un archivo CSV,
    guardarla en la tabla Autor
    y mostrar los datos insertados
"""

import csv
from base_datos import conn

cursor = conn.cursor()

# Ruta del archivo CSV
ruta_csv = "data/info.csv"

print("Leyendo archivo CSV...\n")

# Abrir el archivo CSV
with open(ruta_csv, "r", encoding="utf-8") as archivo:

    lector = csv.DictReader(archivo)

    # Recorrer filas del CSV
    for fila in lector:

        nombre = fila["nombre"]
        apellido = fila["apellido"]
        cedula = fila["cedula"]
        edad = int(fila["edad"])

        # SQL para insertar
        cadena_sql = """
            INSERT INTO Autor (nombre, apellido, cedula, edad)
            VALUES (?, ?, ?, ?)
        """

        cursor.execute(cadena_sql, (nombre, apellido, cedula, edad))

        # Mostrar lo insertado
        print("Insertado:")
        print("Nombre:", nombre)
        print("Apellido:", apellido)
        print("Cédula:", cedula)
        print("Edad:", edad)
        print("---------------------------")

# Guardar cambios
conn.commit()

print("\nDATOS GUARDADOS CORRECTAMENTE\n")

# =========================================
# MOSTRAR TODO LO QUE HAY EN LA TABLA
# =========================================

cursor.execute("SELECT * FROM Autor")

datos = cursor.fetchall()

print("DATOS EN LA BASE DE DATOS:\n")

for d in datos:
    print(
        "ID:", d[0],
        "| Nombre:", d[1],
        "| Apellido:", d[2],
        "| Cédula:", d[3],
        "| Edad:", d[4]
    )

cursor.close()
conn.close()