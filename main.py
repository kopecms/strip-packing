import getopt
import sys

from utils import genarateBoxTuples
from tests import *
from show import showResults, show_single_plot, show_two_plots
from copy import deepcopy
from beam_search import beam_search
from tabu_search import beam_search_tabu


def main(argv):
    width = 90
    offset = 5
    box_quantity = 23
    max_iterations = 20

    try:
        opts, args = getopt.getopt(argv, "hw:o:b:i:", ["width=", "offset=", "boxes=", "iterations="])
        if len(opts) < 1:
            print('No args provided. Run again with -h option to see how to use. Running program with default values')
    except getopt.GetoptError:
        print('main.py -width <magazine width> -offset <offset between boxes> -boxes <number of boxes> -iterations '
              '<number of iterations>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -width <magazine width> -offset <offset between boxes> -boxes <number of boxes> '
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
    store.d = offset
    store.placeBoxesBottomLeftFit(store.boxes)

    store_copy = deepcopy(store)
    top_box = store.getTopBox()
    print("Initial H = {}".format(top_box.y + top_box.h))

    store_beam_search = beam_search(store_copy, max_iterations=max_iterations, max_children=50)
    store_tabu_search = beam_search_tabu(store_copy, max_iterations=max_iterations, max_children=50)

    store_list = [store,
                  store_beam_search,
                  store_tabu_search]

    showResults(store_list)

    store_tabu_search.plot.pop(0)
    li = [store_beam_search.plot[-1]] * (len(store_tabu_search.plot) - len(store_beam_search.plot))
    store_beam_search.plot.extend(li)

    show_single_plot(store_tabu_search.plot, "C0", "Algorytm wspinaczkowy z tabu")
    show_single_plot(store_beam_search.plot, "C1", "Algorytm wspinaczkowy")
    show_two_plots(store_beam_search.plot, store_tabu_search.plot)


if __name__ == "__main__":
    main(sys.argv[1:])
