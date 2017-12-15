from store import Store
from utils import genarateBoxTuples
from tests import *
import unittest
from show import showResults

if __name__ == "__main__":
    #unittest.main()
    store = Store(width=30, boxes=[Box(a) for a in genarateBoxTuples(30)])
    store.placeBoxesBottomLeftFit()
    showResults(store)