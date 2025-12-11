def traverse(depth, lights, expected, maxDepth, buttons):
    if depth == maxDepth:
        return
    
    for button in buttons:
        nextLights = lights.copy()
        for toggleIndex in button:
            current = nextLights[toggleIndex]
            nextLights[toggleIndex] = '#' if current == '.' else '.'

        if nextLights == expected:
            return True

        found = traverse(depth + 1, nextLights, expected, maxDepth, buttons)
        if found:
            return True
        
    return False


pushesTotal = 0
f = open("input.txt")
for line in f:
    parts = line.split(' ')
    expected = list(parts[0][1:-1])
    lights = ['.' for i in range(len(expected))]

    buttons = []
    for i in range(1, len(parts) - 1):
        button = parts[i][1:-1].split(',')
        buttons.append([int(b) for b in button])


    for maxDepth in range(1, 10):
        found = traverse(0, lights, expected, maxDepth, buttons)
        if found:
            pushesTotal += maxDepth
            break

print(pushesTotal)