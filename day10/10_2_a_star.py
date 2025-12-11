import heapq
from collections import namedtuple

Node = namedtuple("Node", "gh g lastButtonId currentState")

pushesTotal = 0
f = open("input.txt")
for line in f:
    if line.startswith('#'):
        continue
    parts = line.split(' ')
    expected = parts[-1][1:-2].split(',')
    expected = tuple(int(n) for n in expected)
    lights = ['.' for i in range(len(expected))]

    buttons = []
    for i in range(1, len(parts) - 1):
        button = parts[i][1:-1].split(',')
        buttons.append([int(b) for b in button])

    buttons.sort(reverse=True, key=lambda x: len(x))
    print(buttons)

    
    openList = [Node(0, 0, -1, tuple(0 for i in expected))]
    closedSet = set()
    heapq.heapify(openList)

    while len(openList) > 0:
        currentNode = heapq.heappop(openList)
        closedSet.add(currentNode.currentState)
        #print(currentNode.currentState)

        # Check if found
        if currentNode.currentState == expected:
            print(currentNode.g)
            break

        numNewButtons = 0
        for buttonId, button in enumerate(buttons):
            newState = list(currentNode.currentState)
            for stepIndex in button:
                newState[stepIndex] += 1

            newState = tuple(newState)
            if newState in closedSet:
                continue

            # Check if overshot and calculate simple h
            invalid = False
            maxDistance = 0
            sumDistances = 0
            for i, slot in enumerate(newState):
                if slot > expected[i]:
                    invalid = True
                    break
                
                distance = expected[i] - slot
                sumDistances += distance
                if distance > maxDistance:
                    maxDistance = distance

            if invalid:
                continue

            newG = currentNode.g + 1
            newNode = Node(newG + sumDistances, newG, buttonId, newState)
            #print(len(openList))
            #print(len(closedSet))
            for node in openList:
                
                if node.currentState == newState:
                    print("Bozo")

            numNewButtons += 1
            heapq.heappush(openList, newNode)

        #print(numNewButtons)

            


