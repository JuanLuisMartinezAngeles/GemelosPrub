'''
Primera snapshot realizada / Branch: Master

Programa el cual lee un diccionario con los datos introducidos a mano y los pasa a un documento con extensión .CSV para su clara lectura llamando a una función.

Promt:
Créame lo siguiente con una función que se ejecute desde otro archivo.
Guardar los datos de un diccionario en un archivo CSV llamado prueba.csv.
Cada clave del diccionario debe ser un encabezado de columna y sus valores deben ir debajo de la columna correspondiente.
El separador de columnas debe ser ;. 
Si el archivo CSV ya existe, los nuevos datos se deben agregar al final, sin sobrescribir los datos existentes. 
Si el archivo no existe, se deben escribir los encabezados antes de los valores.
Al finalizar, mostrar un mensaje indicando que los datos se guardaron correctamente.

*Los nombres dados por la IA utilizada han sido modificados a gusto del usuario.
'''
import csv
import os
import json

def guardar_en_csv(datos, nombre_archivo="prueba.csv"):
    '''
    Guarda un diccionario en un archivo CSV.
    
    Parámetros:
    - datos: diccionario con los datos a guardar
    - nombre_archivo: nombre del archivo CSV (por defecto "prueba.csv")
    
    '''
    archivo_existe = os.path.isfile(nombre_archivo)

    with open(nombre_archivo, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=datos.keys(), delimiter=";")
        
        # Escribir encabezados solo si el archivo no existe
        if not archivo_existe:
            escritor.writeheader()
        
        escritor.writerow(datos)

    print(f"Datos guardados correctamente en '{nombre_archivo}'.")

#Programa el cuál carga/importa los datos de un fichero .json y lo almacena en una variable indicada en la llamada de la fución para su manejo posterior.

def importar_json(nombre_archivo):
    '''
    Carga los datos del fichero .json
    
    Parámetros:
    - nombre_archivo: nombre del archivo json
    
    '''
    
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

#Programa el cual exporta los datos pedidos a  fichero json.

def exportar_json(datos, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
        
    '''
    
    Exporta los datos a el fichero .json
    
    Parámetros:
    - datos: diccionario con los datos a guardar
    - nombre_archivo: nombre del archivo json
    
    '''