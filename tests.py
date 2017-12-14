from unittest import TestCase
from utils import sortBoxesByVolume
from store import Box, Store

boxes_test = [Box((0,0,2,4)), Box((0,0,1,1)),Box((0,0,2,1))]

class TestStore(TestCase):
    def setUp(self):
        self.boxes = boxes_test
        self.box = Box((0,0,4,2))
        # domyslnie d = 1
        self.store = Store()

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


class TestUtils(TestCase):

    def testSortVolume(self):
        boxes = [Box((0,0,1,1)), Box((0,0,2,1)), Box((0,0,2,4))]
        expected = [Box((0,0,2,4)), Box((0,0,2,1)),Box((0,0,1,1))]
        sorted_boxes = sortBoxesByVolume(boxes)
        self.assertEqual([box.getTuple() for box in expected], [box.getTuple() for box in sorted_boxes])
