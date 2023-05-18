#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

diccionario_conteo = {}

for letra in sys.stdin:
  if letra in diccionario_conteo.keys():
    diccionario_conteo[letra] += 1
  else:
    diccionario_conteo[letra] = 1
    
for clave in diccionario_conteo.keys(): 
  print(clave.replace("\n","") + "\t"+str(diccionario_conteo[clave]))
