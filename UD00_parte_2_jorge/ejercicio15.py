import pyperclip
import time
import sys

def load_prohibited_words(file_path):
    """
    Carga las palabras prohibidas desde un archivo.
    Retorna una lista de palabras en minúsculas.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip().lower() for line in file]
    except FileNotFoundError:
        print(f"Error: No s'ha trobat el fitxer {file_path}")
        sys.exit(1)

def censor_text(text, prohibited_words):
    """
    Sustituye las palabras prohibidas por asteriscos en el texto.
    """
    words = text.split()
    censored_words = []
    
    for word in words:
        # Comprobar si la palabra (en minúsculas) está en las prohibidas
        if word.lower() in prohibited_words:
            censored_words.append("*" * len(word))
        else:
            censored_words.append(word)

    return " ".join(censored_words)

def main():
    """
    Programa principal que supervisa el portapapeles.
    """
    if len(sys.argv) != 2:
        print("Ús: python programa.py llista.txt")
        sys.exit(1)

    # Cargar palabras prohibidas
    file_path = sys.argv[1]
    prohibited_words = load_prohibited_words(file_path)
    print(f"Paraules prohibides carregades: {prohibited_words}")

    print("El programa està supervisant el porta-retalls. Prem Ctrl+C per eixir.")
    last_copied = ""

    try:
        while True:
            # Obtener texto del portapapeles
            copied_text = pyperclip.paste()

            # Verificar si el texto ha cambiado
            if copied_text != last_copied:
                censored_text = censor_text(copied_text, prohibited_words)

                # Actualizar portapapeles si es necesario
                if censored_text != copied_text:
                    pyperclip.copy(censored_text)
                    print(f"Text censurat: {censored_text}")

                # Actualizar el último texto copiado
                last_copied = copied_text

            # Esperar un poco antes de comprobar nuevamente
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("\nPrograma finalitzat.")

if __name__ == "__main__":
    main()