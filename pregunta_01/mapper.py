#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import csv
import sys

def separar_depurar(x):
    return(x.split(sep=',')[2])

ruta_archivo=sys.stdin
archivo_leido=[]
with open(ruta_archivo,"rt") as archivo:
    for line in archivo:
        archivo_leido.append(line)
        
sys.stdout.write(list(map(separar_depurar,archivo_leido)))


