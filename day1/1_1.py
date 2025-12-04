position = 50
zeroCount = 0

f = open("1_1.txt")
for line in f:
    direction = line[:1]
    distance = int(line[1:-1])

    if direction == "R":
        position += distance
    if direction == "L":
        position -= distance

    position %= 100
    if position == 0:
        zeroCount += 1

print(zeroCount)