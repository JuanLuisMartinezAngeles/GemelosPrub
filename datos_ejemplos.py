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

'''

from gestion_archivos import guardar_en_csv

d = {
    "Id_Dispositivo": "Dispositivo 1",
    "Estado": "Desconocido",
    "Temperatura": "Buena",
    "Tiempo de ultima medida": "Desconocido",
    "Numero de paquete enviado": "No se sabe"
}

guardar_en_csv(d)

'''



#Programa el cuál carga los datos de un fichero .json y lo almacena en una variable indicada en la llamada de la fución para su manejo posterior.

'''

from gestion_archivos import importar_json 
nombre_archivo = "DB_Alumnos.json"
j = importar_json(nombre_archivo)
print(j[1]["id"]) 

'''