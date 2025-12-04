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
        if length % 2 == 1:
            continue

        # Even, so split in half
        first = numString[: length // 2]
        second = numString[length // 2:]

        if first == second:
            totalSum += i

print(totalSum)