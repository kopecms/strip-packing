from store import Box

def sortBoxesByVolume(boxes):
    return sorted(boxes, key=lambda x: x.v, reverse=True)

def sortBoxesByWidth(boxes):
    return sorted(boxes, key=lambda x: x.w, reverse=True)

