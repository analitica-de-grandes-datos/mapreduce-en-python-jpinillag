#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

diccionario_conteo = {}

for historia_credito in sys.stdin:
  if historia_credito in diccionario_conteo.keys():
    diccionario_conteo[historia_credito] += 1
  else:
    diccionario_conteo[historia_credito] = 1
    
for clave in diccionario_conteo.keys():
  clave_edit=clave.strip()
  string_valor=str(diccionario_conteo[clave])
  print(clave_edit  + "\t" + string_valor)  


