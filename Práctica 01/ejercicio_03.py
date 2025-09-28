""""
3. Generar un nuevo entorno virtual (4 ptos)
Reglas:
- El nombre del entorno virtual tiene que seguir la siguiente estructura  (apellido_nombre)
(mostrar captura de pantalla del entorno virtual vacío)
- Instalar las librerías del requirements.txt obtenido en el problema anterior
en  este nuevo entorno virtual
- Mostrar las librerías instaladas en el nuevo entorno virtual (screemshot)
- Mostrar el proceso de instalación exitoso de todas las dependencias que se
verá en la terminal sobre este nuevo entorno virtual.
- Caso: Calculadora de propinas
Crea un programa que permita ingresar el total de una cuenta en un restaurante,
el porcentaje de propina que desea dejar el cliente y el número de personas que
dividirán la cuenta. El programa debe mostrar:
El monto total con propina.
El monto que debe pagar cada persona (con 2 decimales).
Un mensaje será personalizado, indicará si el monto individual supera los 100
soles, mostrando un mensaje de advertencia si es el caso.
Entrada esperada (por input):
Total de la cuenta: float
Porcentaje de propina: float
Número de personas: int
Salida ejemplo (output):
Monto total con propina: S/. 230.00
Cada persona debe pagar: S/. 115.00
¡Advertencia! El monto por persona supera los S/. 100
"""
total_cuenta = 395.85
porcentaje_propina = 15.75
num_personas = 4

monto_total = total_cuenta + (total_cuenta * porcentaje_propina / 100)
monto_por_persona = monto_total / num_personas

print("Monto total con propina: S/. {:.2f}".format(monto_total))
print("Cada persona debe pagar: S/. {:.2f}".format(monto_por_persona))

if monto_por_persona > 100:
    print("¡Advertencia! El monto por persona supera los S/. 100")