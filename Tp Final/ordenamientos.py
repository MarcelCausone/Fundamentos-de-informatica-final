def ordenar_por_promedio_burbuja(lista):
    datos = lista.copy()
    n = len(datos)
    for i in range(n):
        for j in range(0, n - i - 1):
            try:
                if float(datos[j][5]) > float(datos[j + 1][5]):
                    datos[j], datos[j + 1] = datos[j + 1], datos[j]
            except (IndexError, ValueError):
                continue
    return datos


def ordenar_por_promedio_seleccion(lista):
    datos = lista.copy()
    n = len(datos)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            try:
                if float(datos[j][5]) < float(datos[min_idx][5]):
                    min_idx = j
            except (IndexError, ValueError):
                continue
        datos[i], datos[min_idx] = datos[min_idx], datos[i]
    return datos
