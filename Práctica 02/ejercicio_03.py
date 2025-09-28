"""
Crea un programa en Python que implemente una función llamada  convertir_precio(texto: str) -> float que (4 ptos):
1. Reciba un string que representa un precio en soles (ejemplo: "123.50",  "45", "20.99").
2. Intente convertirlo a un número decimal (float).
3. Tenga las siguientes excepciones:
o Si el texto está vacío, debe lanzar un ValueError("El precio no  puede estar vacío").
o Si el texto contiene caracteres inválidos (ejemplo: "abc",
"12a3"), debe lanzar un ValueError("Formato de precio inválido"). o Si el número es negativo, debe lanzar un ValueError("El precio no  puede ser negativo").
- El programa debe pedir tres precios al usuario, usar la función  convertir_precio y almacenarlos en una lista.
- Finalmente, mostrar:
o La lista con los precios convertidos.
o El precio promedio de los tres valores ingresados.
Ejemplo:
Entrada:
Ingrese precio 1: 100.69
Ingrese precio 2: -45
Ingrese precio 3: abc
Salida:
Error: el precio no puede ser negativo
Error: Formato de precio inválido
Precios válidos ingresados: [100.69]
Promedio: 100.69
"""
def convertir_precio(texto: str) -> float:
    if texto.strip() == "":
        raise ValueError("El precio no puede estar vacío")

    try:
        precio = float(texto)
    except ValueError:
        raise ValueError("Formato de precio inválido")

    if precio < 0:
        raise ValueError("El precio no puede ser negativo")

    return precio


precios = []
for i in range(1, 4):
    entrada = input(f"Ingrese precio {i}: ")
    try:
        precios.append(convertir_precio(entrada))
    except ValueError as error:
        print("Error:", error)

if precios:
    print("Precios válidos ingresados:", precios)
    print("Promedio:", round(sum(precios) / len(precios),2))
else:
    print("No se ingresaron precios válidos")



