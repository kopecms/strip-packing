import heapq
import random
from copy import deepcopy
from utils import removeNotNeededHoles
from algorithm import Node, heuristic


def beam_search( origin, max_iterations=100, max_children=50 ):

    init_node = Node(origin)
    node_list = [ (-1,init_node) ]
    current_node = Node(init_node)
    current_H = current_node.H
    iteration = 0
    plot = []
    while current_H <= current_node.H and iteration < max_iterations:
        iteration += 1
        current_H = current_node.H
        _,current_node = heapq.heappop( node_list ) # select the best node.
        for t in map( heuristic, current_node.generate_children()):
            heapq.heappush( node_list, t )
        node_list = node_list[:max_children]
        plot.append(current_node.H)

    print("Beam search iteration = {}, H = {}".format(max_iterations, current_node.H))
    current_node.store.plot = plot
    return current_node.store






