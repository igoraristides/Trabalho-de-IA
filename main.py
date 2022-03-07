from collections import defaultdict
from turtle import update
from helpers import getNumeroVertice
from depth_First_Search import ddict2dict, dfs
from time import sleep
import os
import time
import keyboard
from tkinter import *
from algoritmoDijkstra import *


#Variável usada Para contar a quantidade de salas visitas --  foi adicionado a pedido da professora
c = 1

def update_Count():
  global c 
  c = c + 1

def menu():
    case = 1000
    while case != 0:
        clear()
        print('~+'*30)
        print('\t\tOLÁ! BEM VINDO(A) AO BLACK ROOM')
        print('~+'*30)

        print('\n\nMENU INICIAL:')
        print('[1]: Iniciar Novo Jogo')
        print('[0]: Sair')

        case = input('\n\nQual opção deseja executar: ')

        def menu2(nameFile):
            case2 = 1000
            while case2 != 0:
                clear()
                print('~+'*40)
                print(
                    '\tESCOLHA O ALGORITMO QUE IRÁ AJUDA-LO(A) A CHEGAR NA ÚLTIMA SALA')
                print('~+'*40)
                print('\n\nMENU:')
                print('[1]: Algoritmo Dijkstra')
                print('[2]: Algoritmo DFS (Busca em Profundidade)')
                print('\n[0]: Sair')

                case2 = input('\n\nQual opção deseja executar: ')

                def dijkstraAlg(file):
                    inicio = time.time()
                    ref_arquivo = open(file, "r")
                    x = []

                    for linha in ref_arquivo:
                        valores = linha.split(",")

                        valores[0] = valores[0].replace('pode_ir(', '')
                        valores[1] = valores[1].strip()
                        valores[2] = valores[2].replace(
                            ').', '').rstrip().strip()

                        valores[0] = valores[0].replace('pode_ir(', '')

                        x.append((valores[0], valores[1], int(valores[2])))

                    g = criarGrafo(x)
                    print('~+'*20)
                    print(
                        '\tALGORITMO DIJKSTRA')
                    print('~+'*20)
                    origem = str(input('\n\tDigite a sala origem: '))
                    destino = str(input('\n\tDigite a sala destino: '))
                   
                    clear()

                    d, prev = algoritmoDijkstra(g, origem, destino)
                    for i in prev:
                        print('~+'*20)
                        print(
                            '\tALGORITMO DIJKSTRA')
                        print('~+'*20)
                        print("\n\n\nSala visitada neste passo ->{}\n\n\n".format(i))
                        print('Pressione Espaço para próxima interação...)')
                        keyboard.wait('space')
                        clear()
                    

                    print('~+'*20)
                    print(
                        '\tALGORITMO DIJKSTRA RESULTADOS')
                    print('~+'*20)
                    print("\n {} ----> {}".format(origem,destino))
                    print("\n A menor distância encontrada foi de: {}\n".format(d))
                    print("\n A(s) sala(s) visitada(s) foram/foi: {}\n".format(prev))
                    print("\n A quantidade de salas visitas foi de : {}\n".format(len(prev)))
                
                    ref_arquivo.close()
                    fim = time.time()
                    print("Tempo de execução do algoritmo:\n")
                    print(fim - inicio)
                    print("\n")

                def dfsAlg(file):
                    inicio = time.time()
                    ref_arquivo = open(file, "r")  # Abertura de arquivo
                    # Instaciando o dicionario que irá guardar o grafo
                    meu_dic = defaultdict(list)

                    for linha in ref_arquivo:
                        # Tratamento do texto escrito no arquivo
                        valores = linha.split(",")

                        valores[0] = valores[0].replace('pode_ir(', '')
                        valores[1] = valores[1].strip()
                        valores[2] = valores[2].replace(
                            ').', '').rstrip().strip()

                        valores[0] = getNumeroVertice(valores[0])
                        valores[1] = getNumeroVertice(valores[1])

                        meu_dic[valores[0]].append(
                            valores[1])  # Atualização do grafo

                        keys = meu_dic.keys()

                        if(valores[1] in keys):
                            continue
                        else:
                            # Tratamento de chave sem valores
                            meu_dic[valores[1]] = []

                    visited = set()
                    print('~+'*20)
                    print(
                        'ALGORITMO DE BUSCA EM PROFUNDIDADE')
                    print('~+'*20)
                    

                    origem = str(input('Digite a sala origem: '))
                    destino = str(input('Digite a sala destino: '))
                    clear()
                    print('~+'*20)
                    print(
                        'ALGORITMO DE BUSCA EM PROFUNDIDADE')
                    print('~+'*20)
                    dfs(visited, ddict2dict(meu_dic), origem, destino, update_Count)
                    print("\n")
                    fim = time.time()
                    print("A quantidade de salas visitas foi de : {}\n".format(c))
                    print("Tempo de execução do algoritmo:\n")
                    print(fim - inicio)
                    print("\n")

                match(case2):
                    case '1':
                        clear()
                        return dijkstraAlg(nameFile)
                    case '2':
                        clear()
                        return dfsAlg(nameFile)
                    case '0':
                        clear()
                        return exitGame()
                    case _defaut:
                        return defaultValue()

        def newGame():
            print("~+" * 40)
            print('\tCARREGUE UM ARQUIVO (.txt) PARA CONFIGURAR AS SALAS DO JOGO!')
            print("~+" * 40)
            nameFile = input('\n\tNome do arquivo (com a extenção .txt): ')
            print('\n\n\tO arquivo ' + nameFile +
                  ' foi carregado com sucesso!')
            print('\n\t\t\tIniciando novo jogo...\n\n')
            #sleep(3)
            menu2(nameFile)

        def exitGame():
            print('\n\nFechando o Jogo e Saindo...\n\n')
            sleep(2.5)
            return

        def defaultValue(c):
            print('A entrada ' + c + ' não é válida aqui!')

        match(case):
            case '1':
                clear()
                return newGame()
            case '0':
                clear()
                return exitGame()
            case _defaut:
                return defaultValue(case)


def clear(): return os.system('cls')


menu()

# conf_salas.txt
