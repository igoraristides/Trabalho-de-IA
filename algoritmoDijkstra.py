from collections import defaultdict


def criarGrafo(arestas):
    grafo_dic = defaultdict(list)
    for origem, destino, peso in arestas:
        grafo_dic[origem].append((destino, peso))
        grafo_dic[destino].append((origem, peso))
    return grafo_dic


def algoritmoDijkstra(grafo_dic, vertice_origem, vertice_destino):
    todosVerticesInDic = getVerticesNoDic(grafo_dic)

    dic_distancia = dict()
    dic_vertice_pai = dict()

    for n in todosVerticesInDic:
        dic_distancia[n] = float('inf')
        dic_vertice_pai[n] = None

    dic_distancia[vertice_origem] = 0

    while todosVerticesInDic:
        vertice_atual = min(todosVerticesInDic, key=dic_distancia.get)
        todosVerticesInDic.remove(vertice_atual)

        if vertice_atual == vertice_destino:
            return dic_distancia[vertice_destino], getCaminhoPercorrido(dic_vertice_pai, vertice_destino)

        if(grafo_dic.get(vertice_atual) is None):
            continue

        for verticeVizinho, peso in grafo_dic.get(vertice_atual):
            nova_distancia = dic_distancia[vertice_atual] + peso
            if nova_distancia < dic_distancia[verticeVizinho]:
                dic_distancia[verticeVizinho] = nova_distancia
                dic_vertice_pai[verticeVizinho] = vertice_atual


def getCaminhoPercorrido(vp, no):
    p = []
    while no is not None:
        p.append(no)
        no = vp[no]
    return p[::-1]


def getVerticesNoDic(grafo):
    vertices = []
    for chave in grafo:
        if(chave in vertices):
            continue
        else:
            vertices.append(chave)
        for vp in grafo[chave]:
            if vp[0] in vertices:
                continue
            else:
                vertices += vp[0]
    return vertices
