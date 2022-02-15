from tkinter import E
from Matriz_Adjacencias import Grafo
import re
from helpers import getNumeroVertice

ref_arquivo = open("conf_salas.txt","r")
values = []
x = []


for linha in ref_arquivo:
    valores = linha.split(",")

    valores[0]=  valores[0].replace('pode_ir(','')
    valores[1]= valores[1].strip()
    valores[2]=  valores[2].replace(').','').rstrip().strip()

    valores [0] = getNumeroVertice(valores[0])
    valores [1] = getNumeroVertice(valores[1])
    x.append(valores) 
    for element in valores:
        if element in values:
            continue
        elementIndex = valores.index(element) 
        if elementIndex ==2:
            continue
        else:
            values.append(element)

g = Grafo(len(values))
for vertice in x:{
         g.adiciona_aresta(int(vertice[0]),int(vertice[1]),int(vertice[2]))
}

result = g.AlgoritmoDijkstra(1)
print(result)
    
ref_arquivo.close()

