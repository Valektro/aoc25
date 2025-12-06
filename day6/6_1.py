f = open("input.txt")
numbers = []
operators = []
for line in f:
    line_splitted = line.split(" ")
    if line_splitted[0] == "*" or line_splitted[0] == "+":
        operators = list(filter(lambda x: x != '', line_splitted))
        break
    
    line_splitted = filter(lambda x: x != '', line_splitted)
    line_splitted = map(lambda x: int(x), line_splitted)
    line_splitted = list(line_splitted)
    numbers.append(line_splitted)

sum = 0
for i in range(len(numbers[0])):
    if operators[i] == '+':
        res = 0
        for j in range(len(numbers)):
            res += numbers[j][i] 
    else:
        res = 1
        for j in range(len(numbers)):
            res *= numbers[j][i] 

    sum += res

print(sum)

