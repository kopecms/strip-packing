from unittest import TestCase
from utils import sortBy
from store import Box, Store
from show import showResults


boxes_test = [Box((0,0,2,4)), Box((0,0,1,1)),Box((0,0,2,1))]


class TestStore(TestCase):
    def showStore(self):
        self.store.boxes = self.store.placed_boxes
        showResults(self.store)

    def setUp(self):
        self.boxes = boxes_test
        self.box = Box((0,0,4,2))
        # domyslnie d = 1
        self.store = Store()
        self.store.optimaze = True

    def testMoveToLeftIfPosible(self):
        self.store.placed_boxes = [Box((0,0,3,3))]
        self.store.holes = [(4,0),]
        self.store.placeBoxesBottomLeftFit([Box((0,0,4,4))])
        expected = [(9, 0), (0, 5), (4, 5)]
        self.assertCountEqual(expected, [hole for hole in self.store.holes])

    def testMoveToLeftIfPosibleButStopOnOtherBox(self):
        self.store.placed_boxes = [Box((0,0,3,3)), Box((4,0,2,2))]
        self.store.holes = [(7,0),]
        self.store.placeBoxesBottomLeftFit([Box((0,0,1,3))])
        expected = [(9, 0), (4, 4), (7, 4)]
        self.assertCountEqual(expected, [hole for hole in self.store.holes])

    def testSimplePlaceBoxesBottomLeftFit(self):
        self.store.placeBoxesBottomLeftFit([Box((0,0,1,1)), Box((0,0,1,1)),Box((0,0,1,1))])
        expected = [(0,0,1,1), (2,0,1,1), (4,0,1,1)]
        self.assertCountEqual(expected, [box.getTuple() for box in self.store.placed_boxes])

    def testAppendHoles(self):
        self.store.placeBoxBottomLeftFit(self.box)
        self.assertNotIn((0,0), self.store.holes)
        self.assertIn((0,3), self.store.holes)
        self.assertIn((5,0), self.store.holes)

    def testSimplePlaceBoxBottomLeftFit(self):
        self.store.width = 6
        self.store.placed_boxes = [Box((4,0,1,1)),]
        self.store.holes = [(0,0), (4,2), (6,0)]
        self.store.placeBoxBottomLeftFit(self.box)
        self.store.placed_boxes.append(self.box)
        self.assertEqual(self.box.position, (0,2))

    def testBoxNotIntersect(self):
        boxes = [Box((0,0,1,1)),Box((2,2,1,1))]
        self.assertFalse(self.store.checkIntersection(boxes[0], boxes[1]))

        boxes = [Box((2,0,1,1)),Box((2,2,1,1))]
        self.assertFalse(self.store.checkIntersection(boxes[0], boxes[1]))

        boxes = [Box((0,0,4,1)),Box((2,2,1,1))]
        self.assertFalse(self.store.checkIntersection(boxes[0], boxes[1]))

    def testBoxIntersect(self):
        boxes = [Box((0,0,1,1)),Box((1,1,1,1))]
        self.assertTrue(self.store.checkIntersection(boxes[0], boxes[1]))

        boxes = [Box((0,0,1,1)),Box((0.5,0.5,1,1))]
        self.assertTrue(self.store.checkIntersection(boxes[0], boxes[1]))

        boxes = [Box((2,2,1,1)),Box((1,1,1,1))]
        self.assertTrue(self.store.checkIntersection(boxes[0], boxes[1]))

    def testPlacment(self):
        self.store.placed_boxes = [Box((0,0,1,1)),Box((2,2,1,1))]
        self.assertTrue(self.store.checkPlacementConditions(Box((0,2,1,1))))

    def testBadPlacment(self):
        self.store.placed_boxes = [Box((0,0,1,1)),Box((2,2,1,1))]

        self.assertFalse(self.store.checkPlacementConditions(Box((0,1,1,1))))
        self.assertFalse(self.store.checkPlacementConditions(Box((0,-2,1,1))))

    def testTopBox(self):
        self.store.placed_boxes = [Box((5,0,1,1)), Box((11,3,2,4)), Box((5,0,2,1))]
        top_box = self.store.getTopBox()
        self.assertTrue(top_box == Box((11,3,2,4)))
