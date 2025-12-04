f = open("input.txt")
lines = f.read().split("\n")

totalRolls = 0
     
lenY = len(lines)
lenX = len(lines[0])
while True:
    removedThisIteration = 0
    for y in range(lenY):
        for x in range(lenX):
            if lines[y][x] == ".":
                continue
            
            # Now check all eight neighbours (Ufff)
            neighbours = 0
            # Top left
            if y > 0 and x > 0 and lines[y - 1][x - 1] == "@":
                neighbours += 1
            # Top 
            if y > 0 and lines[y - 1][x] == "@":
                neighbours += 1
            # Top right
            if y > 0 and x < lenX - 1 and lines[y - 1][x + 1] == "@":
                neighbours += 1
            # Right
            if x < lenX - 1 and lines[y][x + 1] == "@":
                neighbours += 1
            # Bottom right
            if y < lenY - 1 and x < lenX - 1 and lines[y + 1][x + 1] == "@":
                neighbours += 1
            # Bottom
            if y < lenY - 1 and lines[y + 1][x] == "@":
                neighbours += 1
            # Bottom left
            if y < lenY - 1 and x > 0 and lines[y + 1][x - 1] == "@":
                neighbours += 1
            # Left
            if x > 0 and lines[y][x - 1] == "@":
                neighbours += 1

            if neighbours < 4:
                lines[y] = lines[y][:x] + "." + lines[y][x+1:]
                removedThisIteration += 1
                totalRolls += 1

    if removedThisIteration == 0:
        break

print(totalRolls)
