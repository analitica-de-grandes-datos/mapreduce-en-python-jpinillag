#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

diccionario_conteo = {}

for credit_history in sys.stdin:
  if credit_history in diccionario_conteo.keys():
    diccionario_conteo[credit_history] += 1
  else:
    diccionario_conteo[credit_history] = 1
    
for clave in diccionario_conteo.keys():
  clave  = clave .strip()
  linea =  clave  + str(diccionario_conteo[clave])
  sys.stdout.write(linea)  


