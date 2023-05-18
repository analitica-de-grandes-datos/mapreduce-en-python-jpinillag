#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

diccionario_min = {}
diccionario_max = {}

for linea in sys.stdin:
    linea=linea.split(",")
    if linea[0] in diccionario_min:
        if diccionario_min[linea[0]]>linea[1]:
            diccionario_min[linea[0]]=linea[1]
        elif diccionario_max[linea[0]]<linea[1]:
            diccionario_max[linea[0]]=linea[1]
    else:
        diccionario_min[linea[0]]=linea[1]
        diccionario_max[linea[0]]=linea[1]
        
for clave in diccionario_max.keys():
  clave_edit=clave.strip()
  string_max=str(diccionario_max[clave])
  string_min=str(diccionario_min[clave])
  print(clave_edit.replace("\n","")  + "\t" + string_max.replace("\n","")+ "\t" + string_min.replace("\n","")) 
