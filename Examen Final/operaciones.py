import random


def generar_lista():
    try:
        cantidad = int(
            input("Ingrese cuántos números aleatorios desea generar: ")
        )
        lista = [random.randint(1, 100) for _ in range(cantidad)]
        print("Lista generada:", lista)
        indice = int(input("Ingrese un índice para consultar: "))
        print(f"Valor en el índice {indice}: {lista[indice]}")
        return lista
    except ValueError:
        print("Debe ingresar un número entero.")
    except IndexError:
        print("El índice no existe en la lista.")
    return []


def numeros_no_repetidos(lista):
    lista_unica = list(set(lista))
    print("Números no repetidos:", lista_unica)
    return lista_unica


def ordenar_listas(lista):
    mayor_a_menor = sorted(lista, reverse=True)
    menor_a_mayor = sorted(lista)
    print("Orden descendente:", mayor_a_menor)
    print("Orden ascendente:", menor_a_mayor)
    return mayor_a_menor, menor_a_mayor


def mayor_par(lista):
    pares = [n for n in lista if n % 2 == 0]
    if pares:
        mayor = max(pares)
        print("El mayor número par es:", mayor)
        return mayor
    print("No hay números pares en la lista.")
    return None
