
import os
import shutil

extensiones=["dat","py","pdf","txt","csv","jpg","mp4","doc","png"]

for extension in extensiones:
    os.mkdir(extension)
ficheros=os.listdir()

for archivo in ficheros:
    for extension in extensiones:
        if archivo.endswith(f".{extension}"):
            shutil.move(archivo, f".{extension}")

