#Programa el cual realiza las medias de las notas del archivo pasado y lo guarda en otro fichero .json
#+ Prueba de funcionamiento de funcion exportar_json

from gestion_archivos import *

nombre_archivo = "DB_Alumnos.json"

lista_alumnos = importar_json(nombre_archivo)

l = []

'''

Para el fichero que se le pasa se realiza la media de los datos del campo "notas" en cada diccionario de la lista y este resultado se almacena en otro archivo .json.
  
Parámetros:
- nombre_archivo: nombre del archivo .json

'''

for e in lista_alumnos:
    d = {}
    
    media = sum(e["notas"])/len(e["notas"])
    
    d["id"] = e["id"]
    d["nombre"] = e["nombre"]
    d["apellidos"] = e["apellidos"]
    d["edad"] = e["edad"]
    d["notas"] = e["notas"]
    d["nota_media"] = media
    d["faltas"] = e["faltas"]
    d["supera"] = e["supera"]
    
    l.append(d)

exportar_json(l, "Notas_medias.json")