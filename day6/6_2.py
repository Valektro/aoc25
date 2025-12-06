def calc(numbers, operator):
    if operator == '+':
        res = 0
        for num in numbers:
            res += num
    else:
        res = 1
        for num in numbers:
            res *= num

    return res

f = open("input.txt")
lines = f.read().split("\n")

sum = 0
numbers = []
operator = "+"
for i in range(len(lines[0])):
    number = ""
    for j in range(len(lines)):
        digit = lines[j][i]
        if digit == "*":
            operator = "*"
            continue
        if digit == "+":
            operator = "+"
            continue

        if digit != " ":
            number += digit

    if number == "":
        sum += calc(numbers, operator)
        numbers = []
    else:
        numbers.append(int(number))

print(sum)