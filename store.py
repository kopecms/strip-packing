
class Store:
    def __init__(self, width=10, height=0, d=1, boxes=None):
        if boxes is None:
            pass
        self.width = width
        self.d = d
        self.boxes = boxes
        self.placed_boxes = []
        self.height = height

        """
        pomysl mam taki ze do holes trafiaja zawsze po wsaddzeniu boxa:
        (box.x, box.y + box.h + d), (box.x + box.w + d, box.y)
        i jak bedziemy wsadzac kolejnego to trzeba sprawdzic czy
        nie jest przypadkiem mozliwe przesuniecie go w lewo albo w dol
        """
        self.holes = [(0,0),]

    def placeBoxesBottomLeftFit(self):
        pass

    def placeBoxBottomLeftFit(self, box):
        pass

    def checkPlacementConditions(self, box):
        # sprawdza czy box miesci sie w granicach magazynu
        if box.x < 0 or box.x > self.width - box.w or box.y < 0:
            return False

        # box nie moze byc w placed_boxes
        for b in self.placed_boxes:
            if self.checkIntersection(box, b):
                return False
        return True

    def checkIntersection(self, box_one, box_two):
        if not (box_one.x >= box_two.x + box_two.w + self.d or
           box_one.x + box_one.w + self.d <= box_two.x or
           box_one.y >= box_two.y + box_two.h + self.d or 
           box_one.y + box_one.h + self.d <= box_two.y):
            return True

        return False


class Box:
    def __init__(self, box_tuple):
        self.x = box_tuple[0]
        self.y = box_tuple[1]
        self.w = box_tuple[2]
        self.h = box_tuple[3]
        self.v = self.h * self.w

    def getTuple(self):
        return (self.x, self.y, self.h, self.w)

    @property
    def position(self):
        return (self.x, self.y)