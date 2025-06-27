def ordenar_por_promedio_burbuja(lista):     #ordenamiento por burbuja
    datos = lista.copy()    #trabaja sobre una copia
    n = len(datos)
    for i in range(n):
        for j in range(0, n - i - 1):
            try:                                                #compara promedios y hace swap si es necesario
                if float(datos[j][5]) > float(datos[j + 1][5]):
                    datos[j], datos[j + 1] = datos[j + 1], datos[j]
            except (IndexError, ValueError):
                continue    #salta si hay error al comparar
    return datos

#ordenamiento por seleccion (busca el minimo en cada iteracion)
def ordenar_por_promedio_seleccion(lista):
    datos = lista.copy()    #trabaja sobre una copia
    n = len(datos)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            try:        #busca el indice del minimo
                if float(datos[j][5]) < float(datos[min_idx][5]):
                    min_idx = j
            except (IndexError, ValueError):
                continue    #salta si hay error al comparar
        datos[i], datos[min_idx] = datos[min_idx], datos[i] #intercambia el minimo con la posicion actual
    return datos
