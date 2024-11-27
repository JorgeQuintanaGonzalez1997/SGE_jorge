from itertools import permutations

def valido(mesa):
    
    n = len(mesa)
    for i in range(n):
        for j in range(i + 1, n):
            if abs(i - j) == abs(mesa[i] - mesa[j]):
                return False
    return True

def rotacionesYReflejoss(mesa):
    
    n = len(mesa)
    rotaciones = [
        mesa,
        [n - 1 - mesa.index(i) for i in range(n)],  # 90 grados
        mesa[::-1],  # 180 grados
        [n - 1 - mesa[::-1].index(i) for i in range(n)]  # 270 grados
    ]
    reflejos = [
        [n - 1 - i for i in mesa],  # Reflejo horizontal
        [mesa.index(n - 1 - i) for i in range(n)],  # Reflejo vertical
    ]
    return set(tuple(r) for r in rotaciones + reflejos)

def count_queens(n):
   
    soluciones = []
    solucionUnica = set()

    # Generar todas las permutaciones posibles (colocación en columnas)
    for perm in permutations(range(n)):
        if valido(perm):
            soluciones.append(perm)
            # Generar equivalencias por simetría y rotación
            simetria = rotacionesYReflejoss(perm)
            # Añadir solo una representación única
            solucionUnica.add(min(simetria))

    return len(solucionUnica), len(soluciones)

def main():
    """
    Función principal para calcular soluciones de N reinas.
    """
    print(f"{'Tamaño N':<10} {'Soluciones diferentes':<20} {'Soluciones totales'}")
    print("================================================")
    for n in range(4, 11):  # De 4 a 10
        unique_count, total_count = count_queens(n)
        print(f"{n:<10} {unique_count:<20} {total_count}")

if __name__ == "__main__":
    main()