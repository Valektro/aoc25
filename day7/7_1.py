f = open("input.txt")
lines = f.read().split("\n")

countSplitter = 0 
beamsOld = []
for line in lines:
    beamsNew = []
    for i in range(len(line)):
        if line[i] == 'S':
            beamsNew.append(i)
            continue

        if i in beamsOld:
            if line[i] == '^':
                beamsNew.append(i+1)
                beamsNew.append(i-1)
                countSplitter += 1
            else:
                beamsNew.append(i)
            
    beamsOld = beamsNew

print(countSplitter)




        

