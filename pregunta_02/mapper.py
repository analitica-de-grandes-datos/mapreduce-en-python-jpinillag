#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


for fila in sys.stdin:
  fila_separada=fila.split(",")
  sys.stdout.write(fila_separada[3]+","+fila_separada[4]+ "\n")
