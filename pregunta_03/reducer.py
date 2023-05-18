#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

list_registros = []

for linea in sys.stdin:
    linea_separada=linea.split(",")
    list_registros.append((linea_separada[0],linea_separada[1]))
    list_registros=list_registros.sort(key = lambda x: x[1])

for tupla_registro in list_registros:
  print(tupla_registro[0]  + "\t" + str(tupla_registro[1])) 
