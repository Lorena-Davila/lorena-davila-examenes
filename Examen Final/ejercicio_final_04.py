"""
Crear un programa usando decoradores para mostrar solo la hora
y el minuto del momento que se usa el decorador
Reglas:
- Al ejecutar el decorador mostrará un mensaje: “El decorador está siendo
ejecutado a las H con m minutos y S segundos”
- Crear la función decorador adecuadamente que sumará los elementos de la
función que pasará como parámetro de la función decoradora
- Crear una función, por ejemplo: usando 6 números e indicar el mayor de
todos ellos (o x números) para decorarla con la función anterior.
- Usar la propiedad de N parámetros para la función a decorar usando sus key
y values (**kwards) para usar más de 6 valores en la función (value_7 = 10,
value_8 = 22, value_9=45) y visualizar los resultados usando el decorador
implementado con un mínimo tres ejemplos.
"""
from datetime import datetime


def decorador_suma(func):
    def wrapper(*args, **kwargs):
        ahora = datetime.now()
        print(
            f"El decorador está siendo ejecutado a las "
            f"{ahora.hour}h {ahora.minute}m {ahora.second}s."
        )
        total = sum(args) + sum(kwargs.values())
        print(f"Suma total de valores: {total}")
        resultado = func(*args, **kwargs)
        print("La función decorada fue ejecutada correctamente.\n")
        return resultado
    return wrapper


@decorador_suma
def mayor_numero(*args, **kwargs):
    valores_totales = list(args) + list(kwargs.values())
    mayor = max(valores_totales)
    print(f"El número mayor es: {mayor}")
    return mayor


print("Ingrese 6 números:")
valores_ingresados = [float(input(f"Número {i + 1}: ")) for i in range(6)]

mayor_numero(*valores_ingresados, value_7=10, value_8=22, value_9=45)
