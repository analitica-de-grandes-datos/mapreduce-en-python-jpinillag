#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

diccionario={}

for fila in sys.stdin:
    fila_separada=fila.split(";")
    numero=int(fila_separada[0])
    fila_separada[1]=fila_separada[1].strip()
    claves=fila_separada[1].split(",")
    for clave in claves:
       clave=str(clave.replace(" ",""))
       if clave in diccionario.keys():
          diccionario[clave].append(numero)
          diccionario[clave].sort()
       else:
          diccionario[clave]=[numero]

diccionario_ordenado = {}
llaves_ordenadas = sorted(diccionario)
for key in llaves_ordenadas:
  diccionario_ordenado[key] = diccionario[key]
 
for clave in diccionario_ordenado.keys():
    sys.stdout.write(clave + "\t" + str(diccionario_ordenado[clave])[1:-1].replace(" ","")+"\n")
