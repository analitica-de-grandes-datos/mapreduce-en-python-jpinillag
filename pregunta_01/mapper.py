#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


for fila in sys.stdin:
  fila_separada=fila.split(",")
  print(fila_separada[2])


