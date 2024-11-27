'''
Utilitzant la biblioteca https://pypi.org/project/python-barcode/, hem de llegir un fitxer “.csv”
passat per paràmetres de consola.
Aquest fitxer tindrà un format en el qual cada línia usarà “nomalumne,ID”.
Per exemple
“Alumne 01”,”1”
“Alumne 02”,”2”
Haurem de fer un programa, que llegint eixe fitxer “.csv” genere per cada alumne genere un fitxer
“nomalumne.png” amb un codi de barres en format “EAN 13” que tinga com informació el “ID” de
l’alumne
'''
import shutil
import os
import csv
import barcode
import barcode.ean
from barcode.writer import ImageWriter

ean=barcode.ean.EAN13
'''
codigo = "123456789012"
'''


data = [
    ["Alumno01", "1"],
    ["Alumno02", "2"],
    ["Alumno03", "3"],
    ["Alumno04", "4"]
]

with open("archivo.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)  

with open("archivo.csv", mode="r") as file:
    reader = csv.reader(file)
    for row in reader:
        informacion=row
        codigo=str(informacion[1])+str(23456789012)
        if not os.path.exists(f"{informacion[0]}.png"):
            carpeta=os.mkdir(f"{informacion[0]}.png")
        codigo_barras = ean(codigo, writer=ImageWriter())
        nombre_archivo = codigo_barras.save({informacion[0]})
        shutil.move(nombre_archivo,carpeta)
    


