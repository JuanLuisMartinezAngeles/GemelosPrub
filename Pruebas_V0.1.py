## Primera snapshot realizada / Branch: Master
## Programa el cual lee un diccionario con los datos introducidos a mano y los pasa a un documento con extensión .CSV para su clara lectura.

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