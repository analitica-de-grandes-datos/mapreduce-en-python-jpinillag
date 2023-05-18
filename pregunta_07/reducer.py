#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

list=[]

for fila in sys.stdin:
    fila_separada=fila.split(",")
    list.append((fila_separada[0],fila_separada[1],int(fila_separada[2])))
    list.sort(key=lambda x: x[2])
    list.sort(key=lambda x: x[0])


for registro in list:
  sys.stdout.write(registro[0] + "\t" + registro[1]+ "\t" + str(registro[2])+"\n") 
