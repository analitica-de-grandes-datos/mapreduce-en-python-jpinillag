#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import csv

def separar_depurar(x):
    return(x.split(sep=',')[2])


def map_pregunta1():
    
    ruta_archivo="credit.csv"
    archivo_leido=[]
    with open(ruta_archivo,"rt") as archivo:
        for line in archivo:
            archivo_leido.append(line)
    return list(map(separar_depurar,archivo_leido))

map_pregunta1()
