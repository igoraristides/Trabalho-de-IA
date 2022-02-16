from queue import PriorityQueue

class Grafo:
    
    def __init__(self,vertices):
        self.vertices = vertices
        self.grafo = [[0] * self.vertices for i in range(self.vertices)]
        self.visitou = []

    def adiciona_aresta(self,u,v,peso):
            self.grafo[u-1][v-1] = peso

    def mostra_matriz(self):
            print('A matriz adjacência é:')
            for i in range(self.vertices):
                print(self.grafo[i])

    def AlgoritmoDijkstra(self, vertice_inicial):
        c= [[-1, 0] for i in range(self.vertices)]
        c[vertice_inicial - 1] = [0, vertice_inicial]
   
        fila_c_prioridade = PriorityQueue()
        fila_c_prioridade.put((0, vertice_inicial))
        
        while not fila_c_prioridade.empty():
            (dist, vertice_atual) = fila_c_prioridade.get()
            self.visitou.append([vertice_atual])
            for i in range(self.vertices):

                if self.grafo[vertice_atual-1][i] != 0:
                    custo_anterior = c[i][0]
                    novo_custo = dist + self.grafo[vertice_atual-1][i]
                    if(custo_anterior==-1) or (custo_anterior> novo_custo):
                            c[i] = [novo_custo, vertice_atual]
                            fila_c_prioridade.put((novo_custo, i+1))
        return c