from igraph import *

def dijkstra(g, v_inicial, v_final):
    #Inicializar vetor de vertices visitados e distancias
    distancias = {}
    n_visitados = []
    vizinhos = {}

    for i in range(0,len(g.vs())):
        distancias[g.vs[i]] = float("inf") #faz todos os vertices terem distancia grande
        n_visitados.append(g.vs[i]) #nenhum vertice visitado

    distancias[g.vs[v_inicial]] = [0, v_inicial] #no inicial com 0 de distancia

    v_atual = g.vs[v_inicial]

    while len(n_visitados) > 0:
        vizinhos = {}
        for neib in g.neighbors(v_atual, mode="out"):
            weight = g.es[g.get_eid(v_atual, neib, error=False)]['weight']
            peso = weight + distancias[v_atual][0]

            if distancias[g.vs[neib]] == float("inf"):
                distancias[g.vs[neib]] = [peso, v_atual.index]

            else:
                if (distancias[g.vs[neib]][0] > peso):
                    distancias[g.vs[neib]] = [peso, v_atual.index]

            vizinhos[distancias[g.vs[neib]][0]] = neib

        n_visitados.remove(v_atual)

        while (g.vs[vizinhos[min(vizinhos)]] not in n_visitados) and len(vizinhos) > 0:
            del vizinhos[min(vizinhos)]    
            if len(vizinhos) == 0:
                break

        if len(vizinhos) > 0:        
            v_atual = g.vs[vizinhos[min(vizinhos)]]
        else:
            if len(n_visitados) > 0:
                v_atual = n_visitados[0]

    path = []

    print("A distancia minima entre o vertice {} e o vertice {} é de {}".format(v_inicial, v_final, distancias[g.vs[v_final]][0]))
    print("O menor caminho é {}".format(Path(path, g, distancias, v_inicial, v_final)))

    path = path[::-1]
    return path

def Path(path, g, distancias, inicio, fim):
    if fim != inicio:
        path.append(fim)
        return "%s -- > %s" % (Path(path, g, distancias, inicio, distancias[g.vs[fim]][1]), fim)

    else:
        path.append(fim)
        return inicio