from copy import deepcopy
from store import Store
from utils import removeNotNeededHoles

class Node:
    def __init__(self, store):
        self.H = 0
        self.store = store
        self.h_score = 0

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.H < other.H
        return NotImplemented

    def heuristic(self):
        for box in self.store.placed_boxes:
            if self.H < box.y + box.h:
                self.H = box.y + box.h

    def generate_children(self):
        childeren = [self]
        self.store.holes = removeNotNeededHoles(self.store.placed_boxes, self.store.holes)
        for hole in self.store.holes:
            store_copy = deepcopy(self.store)
            store_copy.holes = sorted(store_copy.holes, key=lambda x: (x[1], x[0]))

            box = store_copy.getTopBox()
            box.position = hole
            if box.x < 0 or box.x + box.w > self.store.width or box.y < 0:
                continue
            hole_right = (box.x + box.w + self.store.d, box.y)
            if not hole_right[0] >= self.store.width:
                store_copy.holes.append(hole_right)
            store_copy.holes.append((box.x, box.y + box.h + self.store.d))
            store_copy.holes.append(self.store.moveHoleToLeftIfPosible((box.x, box.y + box.h + self.store.d)))

            store_copy.placed_boxes.remove(box)
            box_itersections = store_copy.findIntersections(box)
            store_copy.placed_boxes.append(box)

            for b in box_itersections:
                store_copy.holes.append((b.x, b.y))
                hole_right = (b.x + b.w + self.store.d, b.y)
                if not hole_right[0] >= self.store.width:
                    store_copy.holes.append(hole_right)
                store_copy.holes.append((b.x, b.y + b.h + self.store.d))
                store_copy.placed_boxes.remove(b)
            store_copy.optimaze = True
            store_copy.placeBoxesBottomLeftFit(box_itersections)

            childeren.append(Node(store_copy))
        return childeren

    def __hash__(self):
        return hash(str(self))

def heuristic( node, goal=20 ):
    node.heuristic()
    node.h_score = abs(node.H-goal)
    return (node.h_score, node)
