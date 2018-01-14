from random import randint

def sortBy(s, t, reverse=True):
    return sorted(s, key=lambda x: (getattr(x, t[0]), getattr(x, t[1])), reverse=reverse)


def genarateBoxTuples(n, w_max = 10, h_max = 10):
    return [(0, 0, randint(1, w_max), randint(1, h_max)) for a in range(n)]


def removeNotNeededHoles(boxes, holes):
    for box in boxes:
        for hole in holes:
            if hole[0] >= box.x and hole[0] <= box.x + box.w and \
               hole[1] >= box.y and hole[1] <= box.y + box.h:
               holes.remove(hole)
    return holes
