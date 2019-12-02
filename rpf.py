from dj import *

def RPF(g, vertice_entrada, vertice_atual, vertice_remetente):
    print("Pacote chegou pelo vertice {} no vertice {}".format(vertice_entrada, vertice_atual))
    path = dijkstra(g, vertice_remetente, vertice_atual)
    if vertice_entrada == path[-2]:
        print("Enviar para todos os enlaces")
    else:
        print("Descartar pacote")
    