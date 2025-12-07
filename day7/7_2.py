f = open("input.txt")
lines = f.read().split("\n")
lines = list(map(lambda line: list(line), lines))
for line in lines:
    for i, val in enumerate(line):
        if val == '.':
            line[i] = 0



for depth in range(1, len(lines)):
    prevLine = lines[depth - 1]
    line = lines[depth]

    for i in range(len(line)):
        if prevLine[i] == 'S':
            line[i] = 1
            continue

        if line[i] == '^':
            line[i - 1] += prevLine[i]
            line[i + 1] += prevLine[i]
        else:
            if prevLine[i] != '^':
                line[i] += prevLine[i]

sum = 0
for d in lines[-1]:
    if isinstance(d, int):
        sum += d

print(sum)