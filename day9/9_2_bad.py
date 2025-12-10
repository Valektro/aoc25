from collections import namedtuple
import math

# Returns orientation which points towards the 'inner' part (green tiles)
# assumes clockwise chaining, and points always being corners
# Orientation can be 'east' (both up and down), 'northeast' (y must be lower), 'southeast' (y must be higher), or 'none
def getValidDirections(p, pLast, pNext):
    # Determine incoming edge orientation
    if pLast.x < p.x:
        inOrientation = 'west' # ->O
    if pLast.x > p.x:
        inOrientation = 'east' # O<-
    if pLast.y < p.y:
        inOrientation = 'north'
    if pLast.y > p.y:
        inOrientation = 'south'

    # Determnie outgoing edge orientation
    if p.x > pNext.x:
        outOrientation = 'west' # <-O
    if p.x < pNext.x:
        outOrientation = 'east' # O->
    if p.y > pNext.y:
        outOrientation = 'north'
    if p.y < pNext.y:
        outOrientation = 'south'

    if inOrientation == 'west' and outOrientation == 'south':
        if outOrientation == 'south':
            return 'none'
        else:
            return 'east'
    if inOrientation == 'north':
        if outOrientation == 'west':
            return 'none'
        else:
            return 'southeast'
    if inOrientation == 'east':
        return 'northeast'
    if inOrientation == 'south':
        if outOrientation == 'east':
            return 'southeast'
        else:
            return 'east'


f = open("input.txt")
Point = namedtuple("Point", "x y")
points = []
for line in f:
    pos = line[:-1].split(",")
    points.append(Point(int(pos[0]), int(pos[1])))

maxArea = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        p1 = points[i] # Left point (has lower x)
        p2 = points[j] # Right point (has higher x)
        if p2.x < p1.x:
            continue

        validOrientation = getValidDirections(p1, points[(i - 1) % len(points)], points[(i + 1) % len(points)])
        if validOrientation == 'none':
            continue
        if validOrientation == 'northeast' and p2.y > p1.y:
            continue
        if validOrientation == 'southeast' and p2.y < p1.y:
            continue

        area = (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)

        if area <= maxArea:
            continue
        
        minX = min(p1.x, p2.x)
        maxX = max(p1.x, p2.x)
        minY = min(p1.y, p2.y)
        maxY = max(p1.y, p2.y)

        invalid = False
        for k in range(len(points)):
            if k == i or k == j:
                continue

            p = points[k]
            xIsBetween = p.x > minX and p.x < maxX
            yIsBetween = p.y > minY and p.y < maxY
            if xIsBetween and yIsBetween:
                invalid = True
                break

            adjIndexes = [(k - 1) % len(points), (k + 1) % len(points)]
            for adjIndex in adjIndexes:
                adjP = points[adjIndex]

                if xIsBetween and p.y == minY and adjP.y > minY:
                    invalid = True
                if xIsBetween and p.y == maxY and adjP.y < maxY:
                    invalid = True
                if yIsBetween and p.x == minX and adjP.x > minX:
                    invalid = True
                if yIsBetween and p.x == maxX and adjP.x < maxX:
                    invalid = True
            
            if invalid:
                break

        if not invalid:
            #print(p1)
            #print(p2)
            maxArea = area

print(maxArea)