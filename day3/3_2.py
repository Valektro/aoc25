NUM_DIGITS = 12
sum = 0

f = open("input.txt")
for line in f:
    line = line[:-1]
    lastIndex = -1
    totalMax = 0

    for cutoff in range(NUM_DIGITS - 1, -1, -1):
        maxNum = 0
        for i in range(lastIndex + 1, len(line) - cutoff):
            num = int(line[i])
            if (num > maxNum):
                lastIndex = i
                maxNum = num

        totalMax = totalMax * 10 + maxNum

    sum += totalMax

print(sum)