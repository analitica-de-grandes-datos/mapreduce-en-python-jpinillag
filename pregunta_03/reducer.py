#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

list = []

for linea in sys.stdin:
  linea_separada = linea.split(",")
  list.append((linea_separada[0],linea_separada[1]))
  list.sort(key=lambda x: x[1])

for tupla in list:
  sys.stdout.write(tupla[0] + "," + str(tupla[1])) 
