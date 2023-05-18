#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

for fila in sys.stdin:
  fila_separada=fila.split("   ")
  sys.stdout.write(fila_separada[1][5:7]+"\n")
