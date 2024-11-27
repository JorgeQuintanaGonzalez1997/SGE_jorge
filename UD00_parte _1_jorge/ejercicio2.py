
def sumar_numeros(a, b):
    return a + b


def doblar_valores_en_lista(lista):
    for i in range(len(lista)):
        lista[i] *= 2


def doblar_valores_y_devolver_copia(lista):
    nueva_lista = [x * 2 for x in lista]
    return nueva_lista


numero1 = 5
numero2 = 10
suma = sumar_numeros(numero1, numero2)
print("Suma de los números:", suma)


mi_lista = [1, 2, 3, 4]
doblar_valores_en_lista(mi_lista)
print("Lista después de modificarla:", mi_lista)


otra_lista = [1, 2, 3, 4]
nueva_lista = doblar_valores_y_devolver_copia(otra_lista)
print("Lista original:", otra_lista)
print("Nueva lista con valores doblados:", nueva_lista)