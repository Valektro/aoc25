f = open("input.txt")
line = f.read()

totalSum = 0

ranges = line.split(",")

for r in ranges:
    r = r.split("-")
    left = int(r[0])
    right = int(r[1])

    for i in range(left, right+1):
        numString = str(i)
        length = len(numString)

        for window in range(1, length // 2 + 1):
            pattern = numString[:window]

            found = True
            for start in range(window, length, window):
                toCheck = numString[start: start + window]
                
                if toCheck != pattern:
                    found = False
                    break

            if found:
                totalSum += i
                break



print(totalSum)