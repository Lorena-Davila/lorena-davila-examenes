"""
Crear un decorador conteo.
Reglas:
- El decorador retornará la cantidad de parámetros que hayas usado en la
función y que a su vez evaluará que deba ser mayor que 1 para procesar esta
lógica, caso contrario indicarlo con un mensaje respectivamente al usuario.
- Al final de la función decorada indicará mediante un mensaje que la función
fue ejecutada exitosamente.
- La función que vas a crear va a capturar, la edad, nombre de un alumno, la
hora y el minuto en que fue registrado (usar la librería correspondiente de
tiempo)
Mostrando un mensaje siguiente: “Pedro de 30 años ha sido registrado a las
16 horas con 20 minutos”
- La función que será decorada también estará pasando 4 notas que calculará
la media del estudiante.
"""
from datetime import datetime


def conteo(func):
    def wrapper(*args, **kwargs):
        total = len(args) + len(kwargs)
        print(f"Cantidad de parámetros usados: {total}")
        if total <= 1:
            print("Debe ingresar más de un parámetro para continuar.")
            return None
        resultado = func(*args, **kwargs)
        print("La función fue ejecutada exitosamente.")
        return resultado
    return wrapper


@conteo
def registrar_alumno(nombre, edad, nota1, nota2, nota3, nota4):
    ahora = datetime.now()
    promedio = (nota1 + nota2 + nota3 + nota4) / 4
    print(
        f"{nombre} de {edad} años ha sido registrado a las "
        f"{ahora.hour} horas con {ahora.minute} minutos."
    )
    print(f"Promedio del estudiante: {promedio:.2f}")
    return promedio


for intento in range(3):
    print(f"\nRegistro {intento + 1}")
    nombre_in = input("Nombre: ")
    edad_in = int(input("Edad: "))
    notas_in = [float(input(f"Nota {i + 1}: ")) for i in range(4)]
    registrar_alumno(nombre_in, edad_in, *notas_in)
