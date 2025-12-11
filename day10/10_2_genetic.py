import random
from datetime import datetime
random.seed(datetime.now().timestamp())
from collections import namedtuple

Button = namedtuple("Button", "mask limit")
Dna = namedtuple("Dna", "score buttonCounts totalDistance pushes")


pushesTotal = 0
resultList = []
f = open("input.txt")
for line in f:
    if line.startswith('#'):
        continue

    parts = line.split(' ')
    expected = parts[-1][1:-2].split(',')
    expected = tuple(int(n) for n in expected)

    buttons = []
    for i in range(1, len(parts) - 1):
        button = parts[i][1:-1].split(',')
        mask = tuple(int(b) for b in button)
        limit = 100000
        for slotIndex in mask:
            if expected[slotIndex] < limit:
                limit = expected[slotIndex]

        buttons.append(Button(mask, limit))

    
    dnas = []
    for i in range(5):
        dnas.append(Dna(10000, tuple(0 for i in buttons), 1000, 1000))

    while True:
        if (dnas[0].totalDistance == 0):
            resultList.append(dnas[0].pushes)
            break

        print(resultList)
        print(dnas[0])
        print(dnas[1])
        print(dnas[2])
        print()
        dnaSet = set()
        for dna in dnas:
            dnaSet.add(dna.buttonCounts)

        for dnaIndex in range(len(dnas)):
            dna = dnas[dnaIndex]
            
            numTries = max(200 // (dnaIndex + 1), 2)
            for addTry in range(numTries):
                newButtonCounts = list(dna.buttonCounts)
                for _ in range(5):
                    for i in range(len(buttons)):
                        if random.randint(0, 100) < 80:
                            continue

                        addSplit = 75 if dna.totalDistance > 50 else 50
                        if random.randint(0, 100) < addSplit:
                            if buttons[i].limit > newButtonCounts[i]:
                                newButtonCounts[i] += 1
                        else:
                            if newButtonCounts[i] > 0:
                                newButtonCounts[i] -= 1

                if tuple(newButtonCounts) in dnaSet:
                    continue

                # Sum up buttons
                result = [0 for i in expected]
                for i in range(len(buttons)):
                    pressed = newButtonCounts[i]
                    for buttonIndex in buttons[i].mask:
                        result[buttonIndex] += pressed

                sumDistances = 0
                for i, slot in enumerate(result):                   
                    distance = abs(expected[i] - slot)
                    sumDistances += distance

                # Calculate score
                numOfPresses = sum(newButtonCounts)
                score = numOfPresses * 0.01 + sumDistances
                dnas.append(Dna(score, tuple(newButtonCounts), sumDistances, numOfPresses))

        print(len(dnas))
        dnas.sort()
        dnas = dnas[:1000]

print("Final result")
print(resultList)