# Finite state machine
"""
Napisz program symulujący działanie automatu skończonego o grafie przejść jak na Rys. 1 (zbiór stanów i
alfabet są takie, jakie wynikają z grafu). Symulujący, czyli pokazujący konfigurację automatu w kolejnych
krokach (graficznie, na grafie). Umożliw podanie dowolnego wejścia (zgodnego z alfabetem).
"""
import networkx as nx
import matplotlib.pyplot as plt
from time import sleep


class StateMachine:
    def __init__(self):
        self.state = 0
        self.acceptable = True if self.state in [0, 4, 5] else False
        self.alphabet = ['a', 'b', 'c']
        self.graph_vis = nx.DiGraph()
        self.edges_and_labels = dict()
        self.graph_dict = {
            0: {
                'a': 2,
                'b': 2,
                'c': 2
                },
            1: {
                'a': 4,
                'b': 0,
                'c': 3
            },
            2: {
                'a': 1,
                'b': 1,
                'c': 6
            },
            3: {
                'a': 3,
                'b': 3,
                'c': 3
            },
            4: {
                'a': 0,
                'b': 5,
                'c': 5
            },
            5: {
                'a': 4,
                'b': 4,
                'c': 4
            },
            6: {
                'a': 3,
                'b': 3,
                'c': 3
            }
        }
        self.create_graph()

    def input_value(self, input):
        for n in input:
            if n not in self.alphabet:
                print('ERROR')
                print('Input not in an ALPHABET')
                quit()
            else:
                self.plot_graph(self.state, input)
                self.state = self.graph_dict[self.state][n]
                print(self.state)

    def create_graph(self):
        for key in self.graph_dict:
            for n in self.graph_dict[key]:
                x = key
                y = self.graph_dict[key][n]
                self.graph_vis.add_edge(x, y)
                if tuple([x, y]) in self.edges_and_labels.keys():
                    self.edges_and_labels[tuple([x, y])] += n
                else:
                    self.edges_and_labels[tuple([x, y])] = n

    def plot_graph(self, current_node, input):
        colors = ['yellow' if node == current_node else 'blue' for node in self.graph_vis.nodes]
        pos = nx.shell_layout(self.graph_vis)
        plt.figure('INPUT: ' + str(input))
        nx.draw_networkx_nodes(self.graph_vis, pos, node_size=500, node_color=colors)
        nx.draw_networkx_labels(self.graph_vis, pos)
        nx.draw_networkx_edges(self.graph_vis, pos, connectionstyle="arc3,rad=0.2",  arrows=True)
        nx.draw_networkx_edge_labels(self.graph_vis, pos, label_pos=0.6, edge_labels=Machine.edges_and_labels)
        plt.show()


Machine = StateMachine()
Machine.input_value('abc')
print('Obecny stan maszyny: ', Machine.state)
print('Czy stan jest akceptowalny: ', Machine.acceptable)
print(Machine.edges_and_labels)
