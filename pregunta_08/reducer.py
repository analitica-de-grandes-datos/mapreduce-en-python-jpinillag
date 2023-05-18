#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

diccionario_conteo = {}
diccionario_suma={}

for linea in sys.stdin:
  linea_separada=linea.split(",")
  if linea_separada[0] in diccionario_conteo.keys():
    diccionario_conteo[linea_separada[0]] += 1
    diccionario_suma[linea_separada[0]]+=int(linea_separada[1])
  else:
    diccionario_conteo[linea_separada[0]] = 1
    diccionario_suma[linea_separada[0]]=int(linea_separada[1])
    
for clave in diccionario_conteo.keys():
  suma=str(diccionario_suma[clave])
  promedio=str(diccionario_suma[clave]/diccionario_conteo[clave])
  sys.stdout.write(clave+"\t"+suma+"\t"+promedio+"\n")
