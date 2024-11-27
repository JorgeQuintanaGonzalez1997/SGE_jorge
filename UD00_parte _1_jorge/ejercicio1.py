
import copy  

lista_original = [1, 2, [3, 4], 5]


copia_superficial = lista_original.copy()

# Copia profunda: se copia toda la estructura, incluyendo listas internas.
copia_profunda = copy.deepcopy(lista_original)


lista_original[2][0] = 99

print("Lista original:", lista_original)       
print("Copia superficial:", copia_superficial)  
print("Copia profunda:", copia_profunda)         


mi_lista = [10, 20, 30]
mi_lista.append(40) 
print("Lista después de agregar un elemento:", mi_lista)


mi_lista.remove(20)  
print("Lista después de quitar un elemento:", mi_lista)


lista_larga = [1, 2, 3, 4, 5, 6, 7, 8]
ultimos_cuatro_elementos = lista_larga[-4:] 
print("Últimos 4 elementos:", ultimos_cuatro_elementos)


frase = "Python es un lenguaje poderoso"
lista_palabras = frase.split()  
print("Lista de palabras:", lista_palabras)







# Comentarios con una sola línea
# Este es un comentario de una sola línea

# Comentarios multilínea
"""
Este es un comentario
que abarca varias
líneas en Python.
"""