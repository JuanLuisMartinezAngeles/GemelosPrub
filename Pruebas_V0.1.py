'''
Primera snapshot realizada / Branch: Master

Programa el cual lee un diccionario con los datos introducidos a mano y los pasa a un documento con extensión .CSV para su clara lectura.

Promt:
Guardar los datos de un diccionario en un archivo CSV llamado prueba.csv.
Cada clave del diccionario debe ser un encabezado de columna y sus valores deben ir debajo de la columna correspondiente.
El separador de columnas debe ser ;. 
Si el archivo CSV ya existe, los nuevos datos se deben agregar al final, sin sobrescribir los datos existentes. 
Si el archivo no existe, se deben escribir los encabezados antes de los valores.
Al finalizar, mostrar un mensaje indicando que los datos se guardaron correctamente.
'''
import csv
import os

d = {
    "Id_Dispositivo": "Dispositivo 1",
    "Estado": "Desconocido",
    "Temperatura": "Buena",
    "Tiempo de ultima medida": "Desconocido",
    "Numero de paquete enviado": "No se sabe"
}


nombre_archivo = "prueba.csv"

archivo_existe = os.path.isfile(nombre_archivo)

with open(nombre_archivo, mode="a", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=d.keys(), delimiter=";")

    if not archivo_existe:
        escritor.writeheader()

    escritor.writerow(d)

print(f"✅ Datos guardados correctamente en '{nombre_archivo}'.")