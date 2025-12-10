from collections import namedtuple
import math

f = open("input.txt")
Point = namedtuple("Point", "x y")
points = []
for line in f:
    pos = line[:-1].split(",")
    points.append(Point(int(pos[0]), int(pos[1])))

maxArea = 0
for i in range(len(points)):
    for j in range(len(points)):
        p1 = points[i] # Left point (has lower x)
        p2 = points[j] # Right point (has higher x)
        if p2.x < p1.x:
            continue

        area = (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)
        if area <= maxArea:
            continue

        minX = min(p1.x, p2.x)
        maxX = max(p1.x, p2.x)
        minY = min(p1.y, p2.y)
        maxY = max(p1.y, p2.y)

        for k in range(len(points)):
            if k == i or k == j:
                continue

            p = points[k]
            pNext = points[(k + 1) % len(points)]
            
            # Vertical edge
            if pNext.x == p.x:    
                if p.x <= minX or p.x >= maxX:
                    continue
                if p.y > minY and p.y < maxY or pNext.y > minY and pNext.y < maxY:
                    break # At least one of the points inside rectangle
                if p.y <= minY and pNext.y >= maxY or pNext.y <= minY and p.y >= maxY:
                    break # Edge intersects rectangle
            # Horizontal edge
            else:               
                if p.y <= minY or p.y >= maxY:
                    continue
                if p.x > minX and p.x < maxX or pNext.x > minX and pNext.x < maxX:
                    break # At least one of the points inside rectangle
                if p.x <= minX and pNext.x >= maxX or pNext.x <= minX and p.x >= maxX:
                    break # Edge intersects rectangle
        else:
            maxArea = area

print(maxArea)