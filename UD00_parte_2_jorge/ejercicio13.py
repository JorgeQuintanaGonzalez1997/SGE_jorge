import requests

def get_characters_by_species(species):
    """
    Obtiene un listado de personajes de la API de Rick and Morty que pertenecen a una especie específica.
    """
    url = "https://rickandmortyapi.com/api/character"
    characters = []
    page = 1

    # Iterar sobre las páginas de resultados
    while True:
        try:
            # Realizar la solicitud GET con los parámetros adecuados
            response = requests.get(url, params={"page": page, "species": species})
            response.raise_for_status()  # Lanza una excepción si la respuesta tiene un error HTTP
            
            data = response.json()
            results = data.get("results", [])
            
            # Añadir los nombres de los personajes a la lista
            for character in results:
                characters.append(character["name"])
            
            # Verificar si hay más páginas
            if data["info"]["next"] is None:
                break
            page += 1

        except requests.exceptions.RequestException as e:
            print(f"Error al obtener los datos: {e}")
            break

    return characters

def main():
    """
    Función principal del programa.
    """
    print("Benvingut a l'explorador de l'univers de Rick and Morty!")
    species = input("Introdueix una espècie (per exemple: Human, Alien, Robot): ").strip()

    print(f"\nBuscant personatges de l'espècie '{species}'...\n")
    characters = get_characters_by_species(species)

    if characters:
        print(f"S'han trobat {len(characters)} personatges de l'espècie '{species}':")
        for i, character in enumerate(characters, start=1):
            print(f"{i}. {character}")
    else:
        print(f"No s'han trobat personatges de l'espècie '{species}'.")

if __name__ == "__main__":
    main()