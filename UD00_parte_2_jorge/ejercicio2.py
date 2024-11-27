

numeros=[1,2,3,4,5,6,7,8,9]

cantidad_1=0
cantidad_2=0
cantidad_3=0
cantidad_4=0
cantidad_5=0
cantidad_6=0
cantidad_7=0
cantidad_8=0
cantidad_9=0

cantidades=[cantidad_1,cantidad_2,cantidad_3,cantidad_4,cantidad_5,cantidad_6,cantidad_7,cantidad_8,cantidad_9]

sudoku_error_fila = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 5],  # El número 5 se repite en la fila 5
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

sudoku_error_columna = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],  # El número 7 se repite en la columna 2
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 7, 5, 2, 8, 6, 1, 7, 9]
]

sudoku_correcto = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]


dic ={1:False,2:False,3:False,4:False,}

def verificarFilas(sudoku):
    error=False
    for fila in sudoku:
        if error==False:
            for numero in fila:
                if error==False:
                    for i in range(9):
                        
                        if numeros[i]==numero:
                            cantidades[i]+=1
                        if cantidades[i]>1:
                            print("Error en las filas")
                            error=True
                            break
            for i in range(9):
                cantidades[i]=0
    if error==False:
        print("Las filas están bien")

def verificarColumnas(sudoku):
    error=False
    for i in range(9):
         if error==False:
            for linea in sudoku:
                if error==False:
                    for j in range(9):
                        if error==False:
                            if numeros[j]==linea[i]:
                                cantidades[j]+=1
                                if cantidades[j]>1:
                                    print("Error en las columnas")
                                    error=True
                                    break
            
                    
            for n in range(9):
                cantidades[n]=0
    if error==False:
        print("Las columnas están bien")      

def verificar_Si_Son_Numeros(sudoku):
    error=False
    for linea in sudoku:
        if error==False:
            for numero in linea:
                if error==False:
                    if numero not in numeros:
                        print("Hay una o varias casillas que no contienen números")
                        error=True
                        break
    print("Todos son números")

def verificarMatrices(sudoku):
    erro=False
    for fila in range (3):
        #Primer cuadrante
        for columna in range(3):
                for i in range(9):
                    if sudoku[fila][columna]==numeros[i]:
                        cantidades[i]+=1
                        if cantidades[i]>1:
                            print("Error en el 1 cuadrante")
                            error=True
                            break
    

    for fila in range (3):
        #Segundo cuadrante
        for columna in range(3,6):
                for i in range(9):
                    if sudoku[fila][columna]==numeros[i]:
                        cantidades[i]+=1
                        if cantidades[i]>1:
                            print("Error en el 2 cuadrante")
                            error=True
                            break

    for fila in range (3):
        #Tercero cuadrante
        for columna in range(6,9):
                for i in range(9):
                    if sudoku[fila][columna]==numeros[i]:
                        cantidades[i]+=1
                        if cantidades[i]>1:
                            print("Error en el 3 cuadrante")
                            error=True
                            break
             
       


verificar_Si_Son_Numeros(sudoku_correcto)


verificarFilas(sudoku_correcto)
verificarColumnas(sudoku_correcto)


verificarFilas(sudoku_error_fila)
verificarColumnas(sudoku_error_columna)
