from igraph import *
import dj
from grafo import *
from rpf import *

#cria o objeto Graph (o grafo)
g = Graph()

g.add_vertices(6) # adicionar 4 vertices ao grafo (indices 0 a 3)
g.add_edges([(0,1), (1,2), (0,2), (2,3), (2,4), (4,5), (1,5)]) #adiciona 4 arestas ao grafo (indices de 0 a 3)

g.vs["name"] = ["v0", "v1", "v2", "v3", "v4", "v5"] #atribui nome aos vertices
g.es["weight"] = [10, 2, 3, 4, 35, 15, 7] #atribui peso as arestas

#mostrando o grafo na tela

g.vs["label"] = g.vs["name"] #rotula os vertices com seus respectivos nomes
g.es["label"] = g.es["weight"] #rotula as arestas com seus respectivos pesos

layout = g.layout("kk") #atribui um layout para a plotagem do grafo

# print(g) #imprime o grafo na linha de comando

# for i in range(0, 6):
#     for j in range(i+1,6):
#         if i != j:
#             dj.dijkstra(g, i, j)

# gra = bell.grafo(6, [(0,1), (1,2), (0,2), (2,3), (2,4), (4,5), (1,5)], ["v0", "v1", "v2", "v3", "v4", "v5"], [10, 2, 3, 4, 35, 15, 7])
# gra.BellmanFord()

tree = grafo(6, [(0,1), (1,2), (0,2), (2,3), (2,4), (4,5), (1,5)], ["v0", "v1", "v2", "v3", "v4", "v5"], [10, 2, 3, 4, 35, 15, 7])
tree.SpanningTree()

#RPF(g, 1, 2, 0)

plot(g,layout = layout) #apresenta o grafo usando interface grafica