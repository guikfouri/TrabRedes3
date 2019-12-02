from igraph import *

class grafo: 

    def __init__(self, vertices, arestas, nomes, pesos): 
        self.g = Graph()    

        self.vertices = vertices
        self.arestas = arestas
        self.pesos = pesos
        self.g.add_vertices(vertices)
        self.g.add_edges(arestas)

        self.g.vs["name"] = nomes
        self.g.es["weight"] = pesos

        self.g.vs["label"] = self.g.vs["name"]
        self.g.es["label"] = self.g.es["weight"]
        self.layout = self.g.layout("kk")

    
    # printar as distâncias
    def printDist(self, dist): 
        print("Distâncias dos vértices ao vertice 0\n") 
        for i in range(self.vertices): 
            print("% d \t\t % d" % (i, dist[i])) 
  
    # função que encontra os menores caminhos do vértice inicial até
    # todos os vértice
    def BellmanFord(self): 

        # setar todas as distâncias à igual a infinito, menos
        # a distância da origem
        dist = [float("Inf")] * self.vertices
        dist[0] = 0
                                
        # encontrar a distância de cada vertice
        for i in range(self.vertices):
            v_atual = self.g.vs[i]
            for neib in self.g.neighbors(v_atual, mode="out"):
                weight = self.g.es[self.g.get_eid(v_atual, neib, error=False)]['weight']

                if dist[i] != float("Inf") and dist[i] + weight < dist[neib]: 
                    dist[neib] = dist[i] + weight 

                if dist[i] > dist[neib] + weight:
                    dist[i] = dist[neib] + weight
            
        # printar dinstancias
        self.printDist(dist) 
        return

    def SpanningTree(self):

        MST = []

        indice_min = self.pesos.index(min(self.pesos))
        MST.append(self.arestas[indice_min])
        del self.arestas[indice_min]
        del self.pesos[indice_min]

        while len(MST) != self.vertices - 1:
            flag1 = 0
            flag2 = 0

            indice_min = self.pesos.index(min(self.pesos))
            for aresta in MST:
                if self.arestas[indice_min][0] in aresta:
                    flag1 = 1
                if self.arestas[indice_min][1] in aresta:
                    flag2 = 1

            if not(flag1 and flag2):
                MST.append(self.arestas[indice_min])
                
            del self.arestas[indice_min]
            del self.pesos[indice_min]

        print ("Lista de arestas que compoe a arvore MST : {}".format(MST))

