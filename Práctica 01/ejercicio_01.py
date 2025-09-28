"""
1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (4 ptos)
Reglas:
- Asignar en variables los datos de tu nombre, salario, edad y compañía para un usuario e identificar
sus tipos de variables.
- Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una  conversión de datos
- Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted  tiene un bono de 10% en el mes de
diciembre” caso contrario mostrar “Usted  tiene un bono del 5% en el mes diciembre”.
- Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su  salario, según corresponda.
"""
nombre = "Lorena Davila"
salario = 3500
edad = "22"
compania = " Falabella"
var_1 = True
var_2 = False

print("Tipo de variable para 'Nombre' es {}".format(type(nombre)))
print("Tipo de variable para 'Salario' es {}".format(type(salario)))
print("Tipo de variable para 'Edad' es {}".format(type(edad)))
print("Tipo de variable para 'Compañia' es {}".format(type(compania)))

bono1 = salario * 0.10
bono2 = salario * 0.05

edad_int = int(edad)

if edad_int > 30:
    print("Usted tiene un bono de 10% en el mes de diciembre:",var_2)

if edad_int <= 30:
    print("Usted tiene un bono del 5% en el mes de diciembre:", var_1)

bono_final = (salario ** 2) + bono2
print("El bono en el mes de diciembre es: {:.2f}".format(bono_final))