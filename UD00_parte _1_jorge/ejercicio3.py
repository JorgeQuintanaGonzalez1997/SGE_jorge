import hashlib


def generar_hash(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


usuarios_lista = []
for i in range(1, 6):
    usuario = f"usuario{i}"
    contrasena = f"password{i}"
    contrasena_hash = generar_hash(contrasena)
    usuarios_lista.append((usuario, contrasena_hash))

print("Lista de usuarios y contraseñas (hash):")
print(usuarios_lista)


def consultar_lista(usuario, contrasena):
    contrasena_hash = generar_hash(contrasena)
    for u, c_hash in usuarios_lista:
        if u == usuario and c_hash == contrasena_hash:
            return True
    return False


print("Consulta 1 (usuario correcto):", consultar_lista("usuario3", "password3"))  
print("Consulta 2 (usuario incorrecto):", consultar_lista("usuario3", "wrongpassword"))  


usuarios_diccionario = {}
for i in range(1, 6):
    usuario = f"usuario{i}"
    contrasena = f"password{i}"
    contrasena_hash = generar_hash(contrasena)
    usuarios_diccionario[usuario] = contrasena_hash

print("\nDiccionario de usuarios y contraseñas (hash):")
print(usuarios_diccionario)


def consultar_diccionario(usuario, contrasena):
    contrasena_hash = generar_hash(contrasena)
    return usuarios_diccionario.get(usuario) == contrasena_hash

print("Consulta 1 (usuario correcto):", consultar_diccionario("usuario3", "password3"))  # True
print("Consulta 2 (usuario incorrecto):", consultar_diccionario("usuario3", "wrongpassword"))  # False