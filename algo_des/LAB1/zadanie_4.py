import networkx as nx
from random import randint
import matplotlib.pyplot as plt


num_of_nodes = 100  # zadana liczba wierzchołków
nodes = list()
G = nx.Graph()
gpos = {}


# petla dodająca wierzchołki do grafu
for n in range(num_of_nodes):
    nodes.append(n)
    G.add_node(n)

# pętla generaująca 3 krawędzie dla każdego z wierzchołków
for x in range(num_of_nodes):
    for n in range(3):
        y = x
        while x == y:
            y = randint(0, num_of_nodes)
        G.add_edge(x, y)

# pętla losująca pozycje
for node in range(num_of_nodes+1):
    for n in range(100):
        position = [randint(0, 8), randint(1, 8)]
        if position not in gpos.values():
            gpos[node] = position
            break
        if n == 99:
            print('Nie udało sięd dopacować wierzchołka.')
            quit()


nx.draw_networkx_nodes(G, gpos, node_size=100)
nx.draw_networkx_labels(G, gpos)
nx.draw_networkx_edges(G, gpos)
plt.show()



