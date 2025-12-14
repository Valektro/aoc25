f = open("input.txt")

graph = {}
for line in f:
    line = line[:-1]
    parts = line.split(' ')
    src = parts[0][:-1]
    destinations = parts[1:]

    graph[src] = destinations

def countPaths(src, dest):
    visited = {} # Maps visited nodes to paths-count

    def traverse(currentNode):
        paths = 0
        for node in graph[currentNode]:
            if node in visited:
                paths += visited[node]
            elif node == dest:
                paths += 1
            elif node == 'out':
                continue
            else:
                paths += traverse(node)

        visited[currentNode] = paths
        return paths

    return traverse(src)
    
print(countPaths('svr', 'fft') * countPaths('fft', 'dac') * countPaths('dac', 'out'))
print(countPaths('svr', 'dac') * countPaths('dac', 'fft') * countPaths('fft', 'out'))
