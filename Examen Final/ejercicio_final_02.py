"""
Utilizar el concepto de módulo necesariamente. Y escribir un programa para el
manejo de listas el cuál cumplirá los siguientes requerimientos (2 ptos):
Reglas:
- Crear una función que le permitirá almacenar X números aleatorios en
una lista y finalmente los imprimirá por consola al llamar la función. X
solo puede ser entero. No otro tipo de dato. Y también un índice
existente en la lista (usar para esto excepciones)
- Crear una función que le permita almacenar los números no repetidos de
la lista anterior, la función retornará este valor para que pueda ser
impreso por consola.
- Crear una función donde se creará una lista para ordenar de mayor a
menor la lista que se creó en el ítem anterior (número no repetidos) y
otra lista para ordenarlas de menor a mayor, retornar este valor e
imprimirlos por consola.
- Crear una función para indicar cuál es el mayor número par de la lista
(lista de la regla 2), retornar este valor e imprimirlo por consola.
- Crear el archivo main.py, donde solo llamarás las anteriores funciones que
se encontrarán alojadas en un módulo (probarlo para dos casos mínimo)
"""
from operaciones import (
    generar_lista,
    numeros_no_repetidos,
    ordenar_listas,
    mayor_par,
)


for caso in range(2):
    print(f"\nCaso {caso + 1}")
    lista = generar_lista()
    if lista:
        lista_unica = numeros_no_repetidos(lista)
        ordenar_listas(lista_unica)
        mayor_par(lista_unica)
