from collections import namedtuple
import math

TEST = False
if TEST:
    INPUT_FILE = "testinput.txt"
else:
    INPUT_FILE = "input.txt"

f = open(INPUT_FILE)
Point = namedtuple("Point", "id x y z")
points = []
for i, line in enumerate(f):
    pos = line[:-1].split(",")
    points.append(Point(i, int(pos[0]), int(pos[1]), int(pos[2])))

Distance = namedtuple("Distance", "distance p1 p2")
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        p1 = points[i]
        p2 = points[j]

        distance = math.sqrt(
            pow(p2.x - p1.x, 2) +
            pow(p2.y - p1.y, 2) +
            pow(p2.z - p1.z, 2)
        )

        distances.append(Distance(distance, i, j))

distances.sort()

groups = []
connectedPoints = set()
index = 0
p1 = 0
p2 = 0
while True:
    # Check exit condition
    if len(connectedPoints) == len(points) and len(groups) == 1:
        break

    p1 = distances[index].p1
    p2 = distances[index].p2
    index += 1
    connectedPoints.add(p1)
    connectedPoints.add(p2)

    p1Group = -1
    p2Group = -1
    for i, group in enumerate(groups):
        if p1 in group:
            p1Group = i
        if p2 in group:
            p2Group = i

    # Same groupId, so ignore or append
    if p1Group == p2Group:
        if p1Group == -1:
            groups.append([p1, p2])
        continue

    # Two groups connect, so merge
    if p1Group != -1 and p2Group != -1:
        groups[p1Group].extend(groups[p2Group])
        groups.pop(p2Group)
        continue

    # Add new point to existing group
    if p2Group == -1:
        groups[p1Group].append(p2)
    elif p1Group == -1:
        groups[p2Group].append(p1)

print(points[p1].x * points[p2].x)