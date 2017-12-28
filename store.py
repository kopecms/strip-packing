from utils import sortBy


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
        self.boxes = sortBy(self.boxes, ('w','h'))
        for box in self.boxes:
            self.placed_boxes.append(self.placeBoxBottomLeftFit(box))

    def placeBoxBottomLeftFit(self, box):
        self.holes = sorted(self.holes, key=lambda x: (x[1], x[0]))
        for i in range(len(self.holes)):
            box.position = self.holes[i]

            if self.checkPlacementConditions(box):
                del self.holes[i]
                self.moveHoleToRightIfBoxPleced(box)
                hole_right = (box.x + box.w + self.d, box.y)
                if not hole_right[0] >= self.width:
                    self.holes.append(hole_right)
                # jesli mozliwe to dziure z lewego górnego roku przesuwamy w lewo
                self.holes.append((box.x, box.y + box.h + self.d))
                self.holes.append(self.moveHoleToLeftIfPosible((box.x, box.y + box.h + self.d)))
                return box
        # Jesli wszystkie hole sa zle to znajdujemy najwyzej polozony box_h
        # umieszczamy nasz na (0,box_h.y + box_h.h + self.d)
        self.placed_boxes = sorted(self.placed_boxes, key=lambda x: x.y+x.h, reverse=True)
        highest_box = self.placed_boxes[0]
        box.position = (0, highest_box.y + highest_box.h + self.d)

    def moveHoleToRightIfBoxPleced(self, box):
        for hole in self.holes:
            if hole[0] >= box.x and hole[0] < box.x + box.w + self.d and \
               hole[1] >= box.y and hole[1] < box.y + box.h + self.d:
                if box.x + box.w + self.d < self.width:
                    self.holes.append((box.x + box.w + self.d, hole[1]))
                self.holes.remove(hole)


    def moveHoleToLeftIfPosible(self, hole):
        if hole[0] == 0:
            return hole
        else:
            new_x = 0
            for b in self.placed_boxes:
                if b.x + b.w + self.d <= hole[0] and hole[1] >= b.y and hole[1] <= b.y + b.h + self.d:
                    new_x = b.x + b.w + self.d
            return (new_x, hole[1])

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

    @position.setter
    def position(self, value):
        self.x, self.y = value
