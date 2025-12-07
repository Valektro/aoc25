f = open("input.txt")
lines = f.read().split("\n")

numTimelines = 0

def traverse(depth, beamIndex):
    global numTimelines
    if depth == len(lines) - 1:
        numTimelines += 1
        print("Timeline detected: " + str(numTimelines))
        return

    if lines[depth][beamIndex] == "^":
        traverse(depth + 1, beamIndex - 1)
        traverse(depth + 1, beamIndex + 1)
    else:
        traverse(depth + 1, beamIndex)

traverse(1, lines[0].find('S'))


print(numTimelines)