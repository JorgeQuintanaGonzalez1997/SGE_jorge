from PIL import Image  
import pytesseract  


imagenRuta = "texto.png"  


imagen = Image.open(imagenRuta)

imagen.show()


texto = pytesseract.image_to_string(imagen)


print("Mostrar texto:")
print(texto)