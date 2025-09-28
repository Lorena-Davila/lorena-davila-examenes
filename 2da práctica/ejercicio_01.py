"""
Escriba un programa donde tendrá los siguientes requisitos (3 ptos):
Reglas:
- Crear una función llamada procesar_notas(estudiantes) la cual va a recibir un diccionario donde
las claves serán los nombres de los estudiantes y sus valores serán listas con 3 notas.
- Calcular el promedio de cada estudiante.
- Devolver un nuevo diccionario donde la clave sea el nombre del estudiante y el valor sea otro
diccionario con:
promedio: que será el promedio de notas
estado: “aprobado” si es mayor o igual a 11, “desaprobado” si es menor - Mostrar en pantalla
el estudiante con mayor promedio
"""
def procesar_notas(lista_estudiantes):
    resultados_finales = {}
    for estudiante, notas in lista_estudiantes.items():
        promedio = sum(notas) / 3

        if promedio >= 11:
            estado = "aprobado"
        else:
            estado = "desaprobado"

        resultados_finales[estudiante] = {
            "promedio": round(promedio, 2),
            "estado": estado
        }
    return resultados_finales

estudiantes = {
    "Diana": [15, 14, 16],
    "Angela": [10, 9, 11],
    "Cielo": [18, 19, 17],
    "Aracely": [8, 7, 9]
}

resultados = procesar_notas(estudiantes)

for nombre, datos in resultados.items():
    print(f"{nombre}: Promedio = {datos['promedio']}, Estado = {datos['estado']}")

nombre_estudiante = ""
mejor_promedio = 0

for nombre, datos in resultados.items():
    if datos["promedio"] > mejor_promedio:
        mejor_promedio = datos["promedio"]
        nombre_estudiante = nombre

print(f"\nEl estudiante con mayor promedio es {nombre_estudiante} con {mejor_promedio}")
