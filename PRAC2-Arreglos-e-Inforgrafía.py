import random
import time

def probar_busqueda(num_alumnos, num_materias, alumno, materia, estructura):
    if estructura == "alumnos_primero":
        matriz = [[random.randint(1, 100) for _ in range(num_materias)] for _ in range(num_alumnos)]
        buscar = lambda: matriz[alumno][materia] 
    else: 
        matriz = [[random.randint(1, 100) for _ in range(num_alumnos)] for _ in range(num_materias)]
        buscar = lambda: matriz[materia][alumno] 
    
    start_time = time.time()
    resultado = buscar()
    return resultado, time.time() - start_time

num_alumnos = int(input("Ingrese el número de alumnos: "))
num_materias = int(input("Ingrese el número de materias: "))
estructura = input("Ingrese la estructura ('alumnos_primero' o 'materias_primero'): ")

if num_alumnos <= 10000:
    alumno = int(input(f"Ingrese el número de alumno (entre 0 y {num_alumnos - 1}): "))
else:
    alumno = 10000

if num_materias <= 100:
    materia = int(input(f"Ingrese el número de materia (entre 0 y {num_materias - 1}): "))
else:
    materia = 100

resultado, tiempo = probar_busqueda(num_alumnos, num_materias, alumno, materia, estructura)

print(f"Resultado de la búsqueda: {resultado}")
print(f"Tiempo de búsqueda con estructura {estructura}: {tiempo:.6f} segundos")
