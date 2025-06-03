import pandas as pd

def ingresar_datos():
    estudiantes = {}
    while True:
        nombre = input("Nombre del estudiante (o 'fin' para terminar): ")
        if nombre.lower() == 'fin':
            break
        try:
            notas = list(map(float, input("Ingresa las calificaciones separadas por comas: ").split(',')))
            estudiantes[nombre] = notas
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")
    return estudiantes

def calcular_promedios(estudiantes):
    promedios = {nombre: sum(notas)/len(notas) for nombre, notas in estudiantes.items()}
    return promedios

def estudiante_top(promedios):
    return max(promedios, key=promedios.get)

def guardar_resultados(estudiantes, promedios, mejor_estudiante):
    with open("resultados.txt", "w") as archivo:
        for nombre, notas en estudiantes.items():
            archivo.write(f"{nombre}: {notas}, Promedio: {promedios[nombre]:.2f}\n")
        archivo.write(f"\nEstudiante con mejor promedio: {mejor_estudiante} ({promedios[mejor_estudiante]:.2f})\n")

def main():
    estudiantes = ingresar_datos()
    promedios = calcular_promedios(estudiantes)
    mejor = estudiante_top(promedios)
    guardar_resultados(estudiantes, promedios, mejor)
    print("Resultados guardados en resultados.txt")

if __name__ == "__main__":
    main()
