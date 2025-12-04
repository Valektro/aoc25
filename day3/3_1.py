sum = 0

f = open("input.txt")
for line in f:
    firstIndex = 0
    firstMax = 0
    for i in range(len(line) - 2):
        num = int(line[i])

        if (num > firstMax):
            firstIndex = i
            firstMax = num

    secondMax = 0
    for i in range(firstIndex + 1, len(line) - 1):
        num = int(line[i])

        if (num > secondMax):
            secondMax = num

    totalMax = firstMax * 10 + secondMax
    sum += totalMax

print(sum)