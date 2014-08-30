# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

EX_GRAPH0 = {0: set([1,2]), 1:set([]), 2:set([])}
EX_GRAPH1 = {0: set([1,4,5]), 1: set([2,6]), 2: set([3]), 3: set([0]), 4:set([1]), 5:set([2]), 6:set([])}
EX_GRAPH2 = {0: set([1,4,5]), 1: set([2,6]), 2: set([3,7]), 3: set([7]), 4:set([1]), 5:set([2]), 6:set([]), 7:set([3]), 8:set([1,2]), 9:set([0,3,4,5,6,7])}


def make_complete_graph(num_nodes):
    """
    This function takes a number and returns a complete graph with that number of nodes
    
    """
    complete = {}
    for nodes in range(0, num_nodes):
        lista = range(num_nodes)
        lista.remove(nodes)
        complete[nodes] = set(lista)
    return complete    
def compute_in_degrees(digraph):
    """

    This function takes a digraph and returns a dictionary with the nodes and each of their own in degrees

    """
    in_degrees = {}
    for key in (digraph):
        total = 0
        for nodes in digraph:
            total = total + (key in digraph[nodes])
        in_degrees[key] = total
    return in_degrees
def in_degree_distribution(digraph):
    """

    This function takesa digraph and returns the distribution of in degrees of the digraph

    """
    degrees = compute_in_degrees(digraph)
    in_degrees = []
    distribution = {}
    for key in degrees:
        in_degrees.append(degrees[key])
    for total in in_degrees:
        distribution[total] = in_degrees.count(total)
    return distribution

