'''
Realitza una aplicació que sol·licite una cadena de text. El programa ha de dir quantes vegades
ocorre cadascun d'aquests patrons sense distingir majúscules i minúscules: “00” “101”, “ABC”,
“HO”. Un caràcter pot formar part de més d'un patró oposat. Per exemple:
En la cadena “000” el patró “00” apareix dues vegades (una comença en la posició 0 i una altra
comença en la posició 1).
Internament, el programa realitzarà el compte de patrons amb una funció definida com
“def numeroPatrones(text)” que retornarà un nombre enter amb el nombre de patrons oposats
'''

cadena_texto=input("Dime una cadena de texto: ")
cadena_texto=cadena_texto.lower()
primer_caracter=''
segundo_caracter=''
tercer_caracter=''
almacenar_caracter=''

contador_00=0
contador_101=0
contador_abc=0


for i,caracter in enumerate (cadena_texto):
    if i==0:
        primer_caracter=caracter
    else:
        tercer_caracter=segundo_caracter
        segundo_caracter=primer_caracter
        primer_caracter=caracter
        if(segundo_caracter+primer_caracter=="00"):
            contador_00+=1
        elif(tercer_caracter+segundo_caracter+primer_caracter=="101"):
            contador_101+=1
        elif(tercer_caracter+segundo_caracter+primer_caracter=="abc"):
            contador_abc+=1
print(f"Cantidad de veces que aparece 00: {contador_00}")
print(f"Cantidad de veces que aparece 101: {contador_101}")
print(f"Cantidad de veces que aparece ABC: {contador_abc}")


