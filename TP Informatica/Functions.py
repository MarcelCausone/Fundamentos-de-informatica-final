import csv
#carga datos del archivo csv a una lista
def cargar_datos():
    with open('notas.csv', newline='', encoding='utf-8') as archivo:
        lector = csv.reader(archivo)
        datos = list(lector)
    return datos

#calcula el promedio de notas por materia
def promedio_por_materia(lista):
    materias = {}
    for fila in lista:
        if len(fila) < 6:
            continue  # salta líneas vacías o incompletas
        materia = fila[1]
        try:
            nota = float(fila[5])
        except ValueError:
            continue  # salta si la nota no es un número válido
        if materia not in materias:
            materias[materia] = []
        materias[materia].append(nota)
    #calcula promedios para cada materia 
    promedios = {}
    for m, n in materias.items():
        promedio = round(sum(n) / len(n), 2)
        promedios[m] = promedio
    return promedios

        
    promedios = {}
    for m, n in materias.items():
        promedio = round(sum(n) / len(n), 2)
        promedios[m] = promedio
    return promedios
#filtra alumnos con nota final mayor al umbral
def nota_mayor_a(lista, umbral):
    resultado = []
    for fila in lista:
        try:
            if float(fila[5]) > umbral:
                resultado.append(fila)
        except (IndexError, ValueError):
            continue  # salta filas con errores
    return resultado
#identifica notas individuales menores a 4
def notas_bajas(lista):
    resultados = []
    for fila in lista:
        if len(fila) < 6:
            continue
        nombre = fila[0]
        materia = fila[1]
        try:   #obtiene las 3 notas
            nota1 = float(fila[2])
            nota2 = float(fila[3])
            nota3 = float(fila[4])
        except ValueError:
            continue
        #verifica cada nota individual
        if nota1 < 4:
            resultados.append((nombre, materia, "Nota 1", nota1))
        if nota2 < 4:
            resultados.append((nombre, materia, "Nota 2", nota2))
        if nota3 < 4:
            resultados.append((nombre, materia, "Nota 3", nota3))
    return resultados

    #cuenta aprobados (nota mayor o igual a 6) y desaprobados (menor a 6)
def contar_aprobados_por_materia(lista):
    conteo = {}

    for fila in lista:
        if len(fila) < 6:
            continue  # evita errores si la fila es incompleta

        materia = fila[1]
        try:
            nota_final = float(fila[5])
        except ValueError:
            continue  # salta si la nota no es un número

        if materia not in conteo:
            conteo[materia] = {"Aprobado": 0, "Desaprobado": 0}
        #clasifica como aprobado o desaprobado
        if nota_final >= 6:
            conteo[materia]["Aprobado"] += 1
        else:
            conteo[materia]["Desaprobado"] += 1

    return conteo


        
        