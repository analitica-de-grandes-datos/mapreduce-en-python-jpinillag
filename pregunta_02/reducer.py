#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

diccionario_maximo = {}

for linea in sys.stdin:
    linea_separada=linea.split(",")
    if   linea_separada[0] in diccionario_maximo.keys():
        if diccionario_maximo[linea_separada[0]] < int(linea_separada[1]):
            diccionario_maximo[linea_separada[0]] = int(linea_separada[1])
    else:
        diccionario_maximo[linea_separada[0]] = int(linea_separada[1])

for clave in diccionario_maximo.keys():
  clave_edit=clave.strip()
  string_valor=str(diccionario_maximo[clave])
  print(clave_edit  + "\t" + string_valor)
