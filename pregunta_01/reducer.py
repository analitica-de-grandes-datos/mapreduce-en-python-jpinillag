#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
from functools import reduce

def conteo(inicial, siguiente):
    inicial[siguiente] = inicial.get(siguiente, 0) + 1
    return inicial
 
def reducer_pregunta1(data):
  return reduce(conteo,data,{})
