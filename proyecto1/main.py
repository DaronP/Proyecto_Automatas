from graphviz import Digraph
from thomson import *
from subconjuntos import *
from libs import *
import sys

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin'


exp = input("Ingrese la expresion regular \n")

exxpr = exp[:0] + '(' + exp[0:]
expr = exxpr[:-1] + ')' + exxpr[-1:]
count = 0

for item in range(len(expr)):
    if expr[item] == '(' or expr[item] == ')':
        count += 1
    
    
if count % 2 == 0:
    print("\Cadena aceptada\n")
else:
    sys.exit('Cadena contiene error')


pos_exp, alfa = postfix(expr)
print("\nEspresion posfix: \n", pos_exp)
print("\nAlfabeto: ", alfa)
thom_resultado, thom_trans = thomson(pos_exp, alfa)
print("\nTransiciones Thompson \n", thom_resultado)
print("\nNodos inicial-final\n", thom_trans)
grafo(thom_resultado, thom_trans, "thomson")
#print(thom_trans)
# print(thom_resultado)
sub_estados, sub_end, minimo, min_end = subconjuntos(thom_resultado, thom_trans)
print("\nTabla de estados: ")
print(sub_estados)
print("\nEstados de inicio/fin: ")
print(sub_end)
print("\nMinimo")
print(minimo)
grafo(sub_estados, sub_end, "subconjuntos")
grafo(minimo, min_end, "minimo")


cadena = input("Ingrese la cadena de caracteres para probar la simulacion\n")

res_t = simulacion(thom_resultado, cadena, thom_trans, alfa, 0)

res_s = simulacion(sub_estados, cadena, sub_end, alfa)

if res_t == 0:
    print("La cadena NO pertenede a THOMSON")

if res_t == 1:
    print("La cadena SI pertenede a THOMSON")

if res_s == 0:
    print("La cadena NO pertenede a SUBCONJUNTOS")
    print("La cadena NO pertenede a MINIMO")

if res_s == 1:
    print("La cadena SI pertenede a SUBCONJUNTOS")
    print("La cadena SI pertenede a MINIMO")