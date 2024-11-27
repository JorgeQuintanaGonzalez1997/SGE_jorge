# Lista inicial con elementos: [altura, peso]
personas = [
    [180, 75],  # Persona 1: altura 180 cm, peso 75 kg
    [165, 65],  # Persona 2: altura 165 cm, peso 65 kg
    [180, 70],  # Persona 3: altura 180 cm, peso 70 kg
    [170, 80],  # Persona 4: altura 170 cm, peso 80 kg
    [180, 85],  # Persona 5: altura 180 cm, peso 85 kg
]

# Ordenamos utilizando sorted() y una key function
# La función clave (key function) define los criterios de ordenación.
personas_ordenadas = sorted(
    personas,
    key=lambda x: (-x[0], x[1])  # Ordenar por altura descendente (-x[0]) y luego peso ascendente (x[1]).
)

# Mostramos el resultado
print("Lista ordenada por mayor altura y, en caso de empate, menor peso:")
for persona in personas_ordenadas:
    print(f"Altura: {persona[0]} cm, Peso: {persona[1]} kg")