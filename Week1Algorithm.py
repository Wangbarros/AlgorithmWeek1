# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

EX_GRAPH0 = {0: [1,2], 1:[], 2:[]}
EX_GRAPH1 = {0: [1,4,5], 1: [2,6], 2: [3], 3: [0], 4:[1], 5:[2], 6:[]}
EX_GRAPH2 = {0: [1,4,5], 1: [2,6], 2: [3,7], 3: [7], 4:[1], 5:[2], 6:[], 7:[3], 8:[1,2], 9:[4,5,6,7]}

def make_complete_graph(num_nodes):
    complete = {}
    for i in range(0, num_nodes):
        lista = range(num_nodes)
        lista.remove(i)
        complete[i] = lista
    print complete
    return complete    
def compute_in_degrees(digraph):
    return 0
def in_degree_distribution(digraph):
    return 0
    
make_complete_graph(2)