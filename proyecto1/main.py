from graphviz import Digraph
from thomson import *
from subconjuntos import *
from libs import *


os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin'

loop = True


while loop:
    expr = input("Ingrese la expresion regular \n")
    if(expr == "nel"):
        break

    
    pos_exp, alfa = postfix(expr)
    print(pos_exp)
    print("Alfabeto: ", alfa)
    thom_resultado, thom_trans = thomson(pos_exp, alfa)
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

    
    