"""
Escriba un programa donde tendrá los siguientes requisitos (4 ptos):
Reglas:

• Clase base Persona
o Atributos: nombre, edad, nacionalidad="peruana", saldo=0.0.
o Métodos para esta clase:
▪ actualizar_nombre(nombre) y actualizar_edad(edad)
(validar edad > 0).
▪ cumplir_anios() (incrementa edad en 1).
▪ mostrar_saldo() (imprime el saldo actual).
▪ transferir(destino, monto) (si no hay fondos
suficientes, imprimir “Saldo insuficiente”; si hay,
basarse en self y acreditar a destino).
• Crear la clase que hereda: Empleado(Persona)
o Atributo adicional: sueldo (float).
o Métodos para esta clase:
▪ aumento_sueldo(porcentaje=0.30) (incrementa el
sueldo en 30% por defecto).
▪ prediccion(anio_objetivo, edad_param=None)
▪ Retorna el mensaje: “En el año XXXX tendrá
XX años”.
▪ Si edad_param se pasa y es menor que
self.edad, imprimir “No es posible realizar la
operación” y no calcular.

• Pruebas mínimas
o Instanciar al menos dos Empleado.
o Aplicar aumento_sueldo 2 veces y mostrar el sueldo
incrementado.
o Realizar una transferencia entre ambos empleados y mostrar
saldos antes y después de ambos

o Probar un caso de saldo insuficiente.
o Usar prediccion(...) con y sin edad_param inválido.
"""
from datetime import datetime


class Persona:
    def __init__(self, nombre, edad, saldo=0.0, nac="Peruana"):
        self.nombre = nombre
        self.edad = edad if edad > 0 else 1
        self.saldo = saldo
        self.nacionalidad = nac

    def transferir(self, destino, monto):
        if monto <= 0 or monto > self.saldo:
            print("Saldo insuficiente o monto inválido.")
        else:
            self.saldo -= monto
            destino.saldo += monto
            print(f"{self.nombre} transfirió S/ {monto:.2f}")

    def mostrar_saldo(self):
        print(f"{self.nombre} tiene S/ {self.saldo:.2f}")


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo, saldo=0.0):
        super().__init__(nombre, edad, saldo)
        self.sueldo = sueldo

    def aumento_sueldo(self, porc=0.3):
        self.sueldo += self.sueldo * porc

    def prediccion(self, anio, edad_param=None):
        actual = datetime.now().year
        if edad_param is not None and edad_param < self.edad:
            print("No es posible realizar la operación.")
        else:
            futura = self.edad + (anio - actual)
            print(f"En {anio} tendrá {futura} años.")


def crear_empleado():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    sueldo = float(input("Sueldo: "))
    saldo = float(input("Saldo inicial: "))
    return Empleado(nombre, edad, sueldo, saldo)


print("Registro de empleados")
emp1 = crear_empleado()
emp2 = crear_empleado()

emp1.aumento_sueldo()
emp2.aumento_sueldo()
emp2.aumento_sueldo()

print("\nAumentos de sueldo")
print(f"{emp1.nombre}: S/ {emp1.sueldo:.2f}")
print(f"{emp2.nombre}: S/ {emp2.sueldo:.2f}")

print("\nTransferencias")
emp1.transferir(emp2, float(input("Monto e1→e2: ")))
emp2.transferir(emp1, float(input("Monto e2→e1: ")))

print("\nSaldos actuales")
emp1.mostrar_saldo()
emp2.mostrar_saldo()

anio = int(input("\nAño para predicción: "))
emp1.prediccion(anio)
emp2.prediccion(anio, edad_param=10)
