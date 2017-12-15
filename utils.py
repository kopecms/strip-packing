from random import randint

def sortBy(s, t, reverse=True):
    return sorted(s, key=lambda x: (getattr(x, t[0]), getattr(x, t[1])), reverse=reverse)

def genarateBoxTuples(n, w_max = 10, h_max = 10):
    return [(0, 0, randint(1, w_max), randint(1, h_max)) for a in range(n)]