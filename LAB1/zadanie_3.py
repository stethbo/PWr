import networkx as nx
import matplotlib.pyplot as plt

# zadana liczba wierzchołków
num_of_nodes = 6

G = nx.complete_graph(num_of_nodes)
position = nx.circular_layout(G)

nx.draw(G, pos=position)
nx.draw_networkx_labels(G, pos=position)
plt.show()
