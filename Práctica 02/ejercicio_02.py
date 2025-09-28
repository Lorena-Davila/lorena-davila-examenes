"""
Usando el concepto de funciones (3 ptos):
Reglas:
- Crear una función normalizar_nombres(nombres)
- El parámetro recibe una lista de string de nombres (6 como mínimo) - Este quitará el espacio
antes y después si lo hubiera
- Convierte en tipo título
- Si hubiera más nombre los debe separar (si debe haber el caso en el input de  datos)
- Devuelve también eliminando duplicados manteniendo el orden de la primera - No mutará la lista original
"""
def normalizar_nombres(nombres):
    lista_final = []
    nombres_vistos = set()

    for texto in nombres:
        nombre_formateado = texto.strip()
        nombre_formateado = nombre_formateado.title()
        lista_nombres = nombre_formateado.split()

        for nombre in lista_nombres:
            if nombre not in nombres_vistos:
                lista_final.append(nombre)
                nombres_vistos.add(nombre)

    return lista_final

nombres_entrada = [
    "  diana  ",
    "angela cielo",
    "MARÍA ",
    "aracely ",
    "cielo",
    "   jose",
    "María"
]

resultado = normalizar_nombres(nombres_entrada)

print("Lista original:", nombres_entrada)
print("Lista normalizada:", resultado)

