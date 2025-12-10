from collections import namedtuple

f = open("input.txt")
Point = namedtuple("Point", "x y")
points = []
for line in f:
    pos = line[:-1].split(",")
    points.append(Point(int(pos[0]), int(pos[1])))

mostLeft = 10000000
mostLeftIndex = -1
mostTop = 10000000
mostTopIndex = -1
mostRight = 0
mostRightIndex = -1
mostBottom = 0
mostBottomIndex = -1

for i, point in enumerate(points):
    current = points[i]
    last = points[(i - 1) % len(points)]
    next = points[(i + 1) % len(points)]

    if abs(current.x - last.x) == 1:
        print("Oh no close x")
    if abs(current.y - last.y) == 1:
        print("Oh no close y")

    if last.x == next.x:
        print("Oh no, same line x")
    if last.y == next.y:
        print("Oh no, same line y")

    if current.x < mostLeft:
        mostLeft = current.x
        mostLeftIndex = i
    if current.x > mostRight:
        mostRight = current.x
        mostRightIndex = i
    if current.y < mostTop:
        mostTop = current.y
        mostTopIndex = i
    if current.y > mostBottom:
        mostBottom = current.y
        mostBottomIndex = i

print("Most Left")
print(mostLeftIndex)
print("Most Top")
print(mostTopIndex)
print("Most Right")
print(mostRightIndex)
print("Most Bottom")
print(mostBottomIndex)

# -> Result: Chain is clockwise