import random


class Car:
    
    def __init__(self, matricula, color):
        self.matricula = matricula
        self.color = color
    
    
    def imprimir(self):
        print(f"Matrícula: {self.matricula}, Color: {self.color}")
    
    
    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
    
    
    def es_color(self, color):
        return self.color == color


def crear_coches(n):
    colores = ["red", "white", "black", "pink", "blue"]
    coches = []
    
    for i in range(1, n + 1):
        color_aleatorio = random.choice(colores)  
        coche = Car(matricula=i, color=color_aleatorio)  
        coches.append(coche)  
    
    return coches


n = int(input("Introduce el número de coches a crear: "))


coches = crear_coches(n)


print("\nDetalles de los coches:")
for coche in coches[:10]:  
    coche.imprimir()