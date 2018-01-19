import getopt
import sys

from utils import genarateBoxTuples
from tests import *
from show import showResults
from copy import deepcopy
from beam_search import beam_search
from tabu_search import beam_search_tabu


def main(argv):
    width = 20
    offset = 1
    box_quantity = 25
    max_iterations = 15

    try:
        opts, args = getopt.getopt(argv, "hw:o:b:i:", ["width=", "offset=", "boxes=", "iterations="])
        if len(opts) < 1:
            print('No args provided. Run again with -h option to see how to use. Running program with default values')
    except getopt.GetoptError:
        print('test.py -width <magazine width> -offset <offset between boxes> -boxes <number of boxes> -iterations '
              '<number of iterations>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -width <magazine width> -offset <offset between boxes> -boxes <number of boxes> '
                  '-iterations <number of iterations>')
            sys.exit()
        elif opt in ("-w", "--width"):
            width = int(arg)
        elif opt in ("-o", "--offset"):
            offset = int(arg)
        elif opt in ("-b", "--boxes"):
            box_quantity = int(arg)
        elif opt in ("-i", "--iterations"):
            max_iterations = int(arg)

    boxes = [Box(a) for a in genarateBoxTuples(box_quantity, w_max=10, h_max=10)]
    store = Store(width, d=offset,  boxes=boxes)
    # store.optimaze = True
    store.d = 2
    store.placeBoxesBottomLeftFit(store.boxes)

    store_copy = deepcopy(store)
    top_box = store.getTopBox()
    print("Initial H = {}".format(top_box.y + top_box.h))
    store_list = [store,
                  beam_search(store_copy, max_iterations=max_iterations, max_children=50),
                  beam_search_tabu(store_copy, max_iterations=max_iterations, max_children=50),
                  ]

    showResults(store_list)


if __name__ == "__main__":
    main(sys.argv[1:])
