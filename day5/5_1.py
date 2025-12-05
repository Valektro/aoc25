f = open("input.txt")

ranges = []
ingredients = []

atRanges = True
for line in f:
    line = line[:-1]
    if line == "":
        atRanges = False
        continue

    if atRanges:
        r = line.split("-")
        ranges.append((int(r[0]), int(r[1])))
    else:
        ingredients.append(int(line))

freshCount = 0
for ingredient in ingredients:
    for r in ranges:
        if ingredient >= r[0] and ingredient <= r[1]:
            freshCount += 1
            break

print(freshCount)