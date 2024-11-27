'''
n Python, una función lambda es una función anónima, es decir, 
que no tiene nombre. Se usa para realizar operaciones simples de manera compacta. 
La sintaxis básica de una función lambda es: lambda argumentos: 
'''


suma = lambda x, y: x + y

resultado = suma(5, 3)
print(resultado)  
'''
map(): Aplica una función a cada elemento de una lista y devuelve una nueva lista con los resultados.

filter(): Filtra los elementos de una lista según una condición dada por una función, y devuelve los elementos que cumplen esa condición.

reduce(): Aplica una función de manera acumulativa a todos los elementos de la lista, reduciéndolos a un único valor (en este caso, el producto de todos los elementos).

'''

from functools import reduce

cadena = input("Introduce una lista de números separados por espacio: ")
numeros = list(map(int, cadena.split()))
numeros_filtrados = list(filter(lambda x: x >= 10, numeros))
producto_total = reduce(lambda x, y: x * y, numeros_filtrados)
print("Lista original:", numeros)
print("Lista filtrada (números >= 10):", numeros_filtrados)
print("Multiplicación de los números filtrados:", producto_total)
