'''
Realitza un programa que rebrà per paràmetres de consola dos noms: el del fitxer d’entrada i el
del fitxer d’eixida.
A més, per tal de tindre aquest programa en un executable i poder distribuir-ho haurem d’empacar
el programa en un executable utilitzant la biblioteca https://www.pyinstaller.org/.
El programa implementarà dues funcions: “esPalindromo” i “esPrimo”.
Important: aquestes funcions hauran d’estar comprovades amb un test unitari. Recomanem per
aquest cas “doctest” https://docs.python.org/es/3/library/doctest.html però val qualsevol altra
utilitat per fer tests unitaris.
El programa ha de llegir el fitxer d’entrada. Aquest fitxer conte un número per línia (no s’especifica
quantes línies, ha de funcionar per qualsevol número).
El nostre programa ha d’imprimir en el fitxer d’eixida dues línies i després un llistat amb un número
per línia:
● La primera línia ha de dir quants números eren “palíndroms” (capicua)
● Una altra línia dient quants eren “cosins”.
● Finalment, “n” línies indicant quins “n” números eren al mateix temps cosins i palíndroms.
Per exemple:
Fitxer “exempleEntrada.txt”
5
7
11
13
14
15
22
Fitxer “exempleEixida.txt”
Hi han 4 números palíndroms.
Hi han 4 números cosins.
5
7
11
'''
def es_palindromo(numero):
    """Verifica si un número es un palíndromo."""
    numero_str = str(numero)
    return numero_str == numero_str[::-1]

def es_primo(numero):
    """Verifica si un número es primo."""
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def procesar_fichero(input_file, output_file):
    """Procesa el archivo de entrada y escribe los resultados en el archivo de salida."""
    try:
        with open(input_file, 'r') as infile:
            numeros = [int(line.strip()) for line in infile if line.strip().isdigit()]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {input_file}")
        return

    palindromos = [n for n in numeros if es_palindromo(n)]
    primos = [n for n in numeros if es_primo(n)]
    comunes = [n for n in palindromos if n in primos]

    with open(output_file, 'w') as outfile:
        outfile.write(f"Hay {len(palindromos)} números palíndromos.\n")
        outfile.write(f"Hay {len(primos)} números primos.\n")
        outfile.write("\n".join(map(str, comunes)))

def main():
    import sys
    if len(sys.argv) != 3:
        print("Uso: python programa.py <archivo_entrada> <archivo_salida>")
        return

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    procesar_fichero(input_file, output_file)
    print(f"Resultados guardados en {output_file}")

if __name__ == "__main__":
    main()