f = open("input.txt")

ranges = []

for line in f:
    line = line[:-1]
    if line == "":
        break

    r = line.split("-")
    ranges.append([int(r[0]), int(r[1])])

# Sort and merge ovelapping ranges
ranges.sort()
index = 0
while True:
    if index >= len(ranges) - 1:
        break

    left = ranges[index]
    right = ranges[index + 1]

    # No overlap
    if left[1] < right[0]:
        index += 1
        continue

    # Merge on overlap
    if right[1] > left[1]:
        left[1] = right[1]
    ranges.pop(index + 1)

# Sum up ranges
sum = 0
for r in ranges:
    sum += r[1] - r[0] + 1

print(sum)