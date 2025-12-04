import sys

position = 50
zeroCount = 0

f = open("max_input.txt")
for line in f:
    direction = line[:1]
    distance = int(line[1:-1])

    while True:
        if direction == "R":
            position += 1
        if direction == "L":
            position -= 1

        position %= 100
        distance -= 1

        if position == 0:
            zeroCount += 1

        if distance == 0:
            break

print(zeroCount)