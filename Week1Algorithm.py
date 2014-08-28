# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

EX_GRAPH0 = {0: set([1,2]), 1:set([]), 2:set([])}
EX_GRAPH1 = {0: set([1,4,5]), 1: set([2,6]), 2: set([3]), 3: set([0]), 4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0: set([1,4,5]), 1: set([2,6]), 2: set([3,7]), 3: set([7]), 4:set([1]), 5:set([2]), 6:set([]), 7:set([3]), 8:set([1,2]), 9:set([0,3,4,5,6,7])}

def make_complete_graph(num_nodes):
    complete = {}
    for i in range(0, num_nodes):
        lista = range(num_nodes)
        lista.remove(i)
        complete[i] = set(lista)
    print complete
    return complete    
def compute_in_degrees(digraph):
    return 0
def in_degree_distribution(digraph):
    return 0
    
make_complete_graph(2)