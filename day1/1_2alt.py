position = 50
zeroCount = 0

f = open("1_1.txt")
for line in f:
    direction = line[:1]
    distance = int(line[1:-1])

    # Full hundreds
    zeroCount += distance // 100
    distance %= 100
    if distance == 0:
        continue

    posStartsAtZero = position == 0

    if direction == "R":
        position += distance
        
    if direction == "L":
        position -= distance

    if position >= 100 or position <= 0 and not posStartsAtZero:
        zeroCount += 1

    position %= 100
    
print(zeroCount)