from store import Store
from utils import genarateBoxTuples
from tests import *
import unittest
from show import showResults
from copy import deepcopy
import algorithm
from beam_search import beam_search
from tabu_search import beam_search_tabu


if __name__ == "__main__":
    store = Store(width=20, boxes=[Box(a) for a in genarateBoxTuples(25, w_max = 10, h_max = 10)])
    # store.optimaze = True
    store.d = 2
    store.placeBoxesBottomLeftFit(store.boxes)

    store_copy = deepcopy(store)
    top_box = store.getTopBox()
    print("Initial H = {}".format(top_box.y + top_box.h))
    store_list = [store,
                beam_search(store_copy, max_iterations=15, max_children=50),
                beam_search_tabu(store_copy, max_iterations=15, max_children=50),
                ]

    showResults(store_list)