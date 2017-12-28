import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

from store import Box, Store

boxes_test = [Box((0,0,1,1)),Box((2,2,1,1))]


def showResults(store=Store(width=10, height=10, boxes=boxes_test)):
    fig, ax = plt.subplots()
    Path = mpath.Path
    
    # draw store
    store_path = path_data = [
        (Path.MOVETO, (0, store.height)),
        (Path.LINETO, (0, 0)),
        (Path.LINETO, (store.width, 0)),
        (Path.CLOSEPOLY, (store.width, store.height)),
    ]
    codes, verts = zip(*path_data)
    path = mpath.Path(verts, codes)
    x, y = zip(*path.vertices)
    line, = ax.plot(x, y, 'go-')

    # draw boxes
    for box in store.boxes:
        path_data = [
            (Path.MOVETO, (box.x, box.y)),
            (Path.LINETO, (box.x, box.y + box.h)),
            (Path.LINETO, (box.x + box.w, box.y + box.h)),
            (Path.LINETO, (box.x + box.w, box.y)),
            (Path.CLOSEPOLY, (box.x, box.y)), 
        ]
        codes, verts = zip(*path_data)
        path = mpath.Path(verts, codes)
        x, y = zip(*path.vertices)
        line, = ax.plot(x, y, 'go-')

    # draw holes
    for hole in store.holes:
        ax.plot(hole[0], hole[1], 'o')
    
    ax.grid()
    ax.axis('equal')
    plt.show()
