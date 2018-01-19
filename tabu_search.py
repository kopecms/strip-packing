import heapq
import random
from algorithm import Node, heuristic


def beam_search_tabu( origin, tabu_size=5, max_iterations=1000, max_children=20):

    init_node = Node(origin)
    node_list = [ (-1,init_node) ]
    current_node = Node(init_node)
    tabu_set = []
    plot = []

    iteration = 0
    while iteration < max_iterations:
        iteration += 1
        _, current_node = heapq.heappop( node_list ) # select the best node.
        while hash(current_node) in tabu_set:
              _, current_node = heapq.heappop( node_list ) # select the best node.
        tabu_set = [hash(current_node)] + tabu_set[:tabu_size-1]

        for node in current_node.generate_children():
            if hash(node) not in tabu_set:
                heapq.heappush( node_list, ( heuristic( node ), node))
        node_list = node_list[:max_children]
        plot.append(current_node.H)


    print("Tabu search for {} iteration found H equal to {}".format(max_iterations, current_node.H))
    current_node.store.plot = plot
    return current_node.store





