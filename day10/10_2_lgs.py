from collections import namedtuple

INPUT_FILE = "input.txt"
AT_INDEX_ONLY = None

def printMatrix(matrix):
    for row in matrix:
        print(*row, sep="\t")

# Mutates changeRow
def subtractRows(baseRow, changeRow, colIdx):
    baseRow = baseRow.copy()

    baseRowCoefficient = baseRow[colIdx]
    changeRowCoefficient = changeRow[colIdx]
    for cIdx in range(colIdx, len(baseRow)):
        # Multiply coefficients of colIdx, so they can be eliminated by substraction
        baseRow[cIdx] *= changeRowCoefficient
        changeRow[cIdx] *= baseRowCoefficient
        # Now subract
        changeRow[cIdx] -= baseRow[cIdx]

def eliminateEmptyRows(matrix, rowIdx):
    checkRowIdx = rowIdx + 1
    while checkRowIdx < len(matrix):
        onlyZeros = True
        for cIdx in range(len(matrix[0])):
            if matrix[checkRowIdx][cIdx] != 0:
                onlyZeros = False
                break

        if onlyZeros:
            matrix.pop(checkRowIdx)
        else:
            checkRowIdx += 1
    
def divideRowsByCommonDenominator(row, denominator):
    while True:
        # first check if can divide by denominator
        for entry in row:
            if entry % denominator != 0:
                return

        # Now divide entries by denominator
        for i in range(len(row)):
            row[i] //= denominator

def findFirstNotNullIndex(row):
    for i in range(numButtons):
        if row[i] != 0:
            return i
    else:
        print("Don't know how to handle that")
        return 0

f = open(INPUT_FILE)
totalPushes = 0
for lineNumber, line in enumerate(f):
    if AT_INDEX_ONLY is not None and lineNumber != AT_INDEX_ONLY:
        continue
    if line.startswith('#'):
        continue
    parts = line.split(' ')
    expected = parts[-1][1:-2].split(',')
    expected = tuple(int(n) for n in expected)

    buttons = []
    for i in range(1, len(parts) - 1):
        button = parts[i][1:-1].split(',')
        buttons.append([int(b) for b in button])
    numButtons = len(buttons)

    # Build initial matrix: 
    # - has rank rows and 
    # - numButtons + 1 columns (the rightmost has expected)
    matrix = []
    for i in range(len(expected)):
        row = []
        for j in range(numButtons):
            button = buttons[j]
            row.append(1 if i in button else 0)
        row.append(expected[i])
        matrix.append(row)

    

    # Build stepped form
    rowIdx = 0
    while rowIdx < min(len(matrix), numButtons):
        # At first reorder, so rows with earlier one's are more above
        matrix.sort(reverse=True, key=lambda array: [abs(x) for x in array])
        
        # Keep numbers small
        for rIdx in range(rowIdx, len(matrix)):
            divideRowsByCommonDenominator(matrix[rIdx], 2)
            divideRowsByCommonDenominator(matrix[rIdx], 3)

        # Determine column of next non-0 coefficient
        colIdx = findFirstNotNullIndex(matrix[rowIdx])

        # Now simplify all rows below, so that they are 0 at colIdx     
        for nextRowIdx in range(rowIdx + 1, len(matrix)):
            # Skip if coefficient at colIdx is 0
            if matrix[nextRowIdx][colIdx] == 0:
                continue
            baseRow = matrix[rowIdx]
            changeRow = matrix[nextRowIdx]
            subtractRows(baseRow, changeRow, colIdx)
        
        # Eliminate full-zero rows
        eliminateEmptyRows(matrix, rowIdx)
        
        rowIdx += 1


    # Now set in solutions bottom-up
    # Extend matrix
    for row in matrix:
        row.extend([0 for i in range(numButtons)])

    for rowIdx in range(len(matrix) - 1, -1, -1):
        baseRow = matrix[rowIdx]
        # Determine column of next non-0 coefficient
        colIdx = findFirstNotNullIndex(baseRow)

        # First divide by coefficient (so it becomes 1)
        coefficient = baseRow[colIdx]
        for nextColIdx in range(colIdx, 2 * numButtons + 1):
            baseRow[nextColIdx] /= coefficient
            
        # Bring all other coefficients to the other side
        for nextColIdx in range(colIdx + 1, numButtons):
            baseRow[nextColIdx + numButtons + 1] -= baseRow[nextColIdx]
            baseRow[nextColIdx] = 0

        # No set in scalar at colIdx in all rows above, so it is resolved
        for nextRowIdx in range(rowIdx - 1, -1, -1):
            # Skip if coefficient at colIdx is 0
            if matrix[nextRowIdx][colIdx] == 0:
                continue
            changeRow = matrix[nextRowIdx]
            subtractRows(baseRow, changeRow, colIdx)


    # Insert missing buttons
    rowIdx = 0
    for rowIdx in range(numButtons):
        if rowIdx >= len(matrix) or matrix[rowIdx][rowIdx] == 0:
            newRow = [0 for i in range(2 * numButtons + 1)]
            newRow[rowIdx] = 1
            newRow[rowIdx + numButtons + 1] = 1
            matrix.insert(rowIdx, newRow)
    
    # Remove left part (we don't need it anymore)
    baseColumn = []
    for rowIdx in range(len(matrix)):
        matrix[rowIdx] = matrix[rowIdx][numButtons:]
        baseColumn.append(matrix[rowIdx][0])
        matrix[rowIdx] = matrix[rowIdx][1:]


    # Determine remaining "param-button-Indexes"
    paramButtonIds = []
    for buttonId in range(numButtons):
        for row in matrix:
            if row[buttonId] != 0:
                paramButtonIds.append(buttonId)
                break


    # Make simple dfs tree traversal
    def traverse(paramIdx, setParams):
        if paramIdx == len(paramButtonIds):
            resultColumn = baseColumn.copy()
            for paramIdx, param in enumerate(setParams):
                paramButtonId = paramButtonIds[paramIdx]
                for rowIdx, row in enumerate(matrix):
                    coefficient = row[paramButtonId]
                    resultColumn[rowIdx] += coefficient * param

            # Check for negative pushes (not allowed)
            for val in resultColumn:
                if val < 0 or not (abs(val - round(val)) < 1e-5):
                    #print(resultColumn)
                    return 10000000


            # Calculate button presses
            return sum(resultColumn)
        
        minPushes = 10000000
        for i in range(0, 200):
            newParams = setParams.copy()
            newParams.append(i)
            pushes = traverse(paramIdx + 1, newParams)
            if pushes < minPushes:
                minPushes = pushes

        return minPushes

    pushes = traverse(0, [])
    totalPushes += pushes
    print("Pushes: " + str(pushes))

print()
print("Total pushes: " + str(totalPushes))