#Variável & função  para definir quando para a recursão, pois do jeito que estava ele percorria todas as salas 
state = True

def stopR():
  global state 
  state = False


def ddict2dict(d):
    for k, v in d.items():
        if isinstance(v, dict):
            d[k] = ddict2dict(v)
    return dict(d)


def dfs(visited, graph, node, nodeD, update):
    print('->', end=" ")
    print(node, end=" ")

    if node not in visited:
        visited.add(node)
        if node == nodeD:
            stopR() #foi necessário por para parar a recursão, pois só parava quando passava por todas as salas 
            return
        for neighbour in graph[node]:
            if(state ==True):
                update() #foi necessário para contar a quantidade de salas visitadas, como solicitado pela professora
                dfs(visited, graph, neighbour, nodeD, update)

           
# função anterior demonstrada para professora e com erro

# def dfs(visited, graph, node, nodeD):
#     print('->', end=" ")
#     print(node, end=" ")
#     if node not in visited:
#         visited.add(node)
#         if node == nodeD:
#             return
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour, nodeD)
