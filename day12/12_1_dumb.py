f = open("input.txt")
lines = f.read().split('\n')
FACTOR = 1 # Factor can be between 1 and 1.3 (yes, this task is just stupid)

blockSizes = []
i = 0
while i < 30:
    blockCount = 0
    blockCount += lines[i + 1].count('#')
    blockCount += lines[i + 2].count('#')
    blockCount += lines[i + 3].count('#')
    blockSizes.append(blockCount)
    i += 5

fitInCount = 0
for i in range(30, len(lines) - 1):
    parts = lines[i].split(' ')
    area = parts[0][:-1].split('x')
    area = list(map(lambda x: int(x), area))
    areaSize = area[0] * area[1]
    blockCounts = list(map(lambda x: int(x), parts[1:]))
    
    occupiedFields = 0
    for i, blockCount in enumerate(blockCounts):
        occupiedFields += blockCount * blockSizes[i]

    if occupiedFields * FACTOR < areaSize:
        fitInCount += 1

print(fitInCount)