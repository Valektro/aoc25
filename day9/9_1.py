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
    for j in range(i + 1, len(points)):
        p1 = points[i]
        p2 = points[j]
        area = (abs(p1.x - p2.x) + 1) * (abs(p1.y - p2.y) + 1)

        if area > maxArea:
            maxArea = area

print(maxArea)