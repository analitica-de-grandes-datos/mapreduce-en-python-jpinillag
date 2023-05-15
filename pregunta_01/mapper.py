#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


for fila in sys.stdin:
  fila_separada = fila.split(",")
  credit_history = fila_separada[2]
  sys.stdout.write(credit_history+"\n")


