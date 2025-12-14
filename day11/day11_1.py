f = open("input.txt")

graph = {}
for line in f:
    line = line[:-1]
    parts = line.split(' ')
    src = parts[0][:-1]
    destinations = parts[1:]

    graph[src] = destinations

paths = 0
def traverse(currentNode):
    global paths
    if currentNode == 'out':
        paths += 1
        return
    
    for node in graph[currentNode]:
        traverse(node)


traverse('you')

print(paths)
