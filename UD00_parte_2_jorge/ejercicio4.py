buscaminas = [
    [ 0,  0,  0,  0,  0,  0, -1,  0],
    [ 0, -1,  0,  0, -1,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0, -1],
    [ 0, -1,  0,  0, -1,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0, -1,  0,  0,  0, -1,  0],
    [-1,  0,  0,  0, -1,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0, -1]
]

# Imprimir el tablero

for e in buscaminas:
    print(e)
print("============")
def pistaMinas(buscaminas):
    longitudFila=len(buscaminas)
    ubicacionMinas=[]
    alrededorDeLaMina=[[-1,+1],[-1,0],[-1,-1],[0,-1],[0,+1],[+1,+1],[+1,0],[+1,-1]]
    
    for i,fila in enumerate(buscaminas):
        for j,numero in enumerate(fila):
            if numero == -1:
                ubicacionMinas.append([i,j])
    
    for mina in ubicacionMinas:
        for n in alrededorDeLaMina:
            try:
                if buscaminas[mina[0]+n[0]][mina[1]+n[1]] !=-1:
                    print(f"Posicion 7,7: {buscaminas[7][7]} Movimiento: {n}")
                    buscaminas[mina[0]+n[0]][mina[1]+n[1]]+=1
                    
                   
            except Exception: 
                continue
                
    

    
    return buscaminas
        
        
                
resultado=pistaMinas(buscaminas)

for a in resultado:
    print(a)



    
