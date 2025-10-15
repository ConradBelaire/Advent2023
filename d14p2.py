import numpy as np

f = open("d14_input.txt", "r")
field = []

def printField(input):
    for row in input:
        print(''.join(row))
    print()

while True:
    line = f.readline()
    if line == "\n":
        break
    if not line:
        eof = True
        break
    field.append(list(line.strip()))
printField(field)
#printField(np.rot90(field).tolist())

def rollNorth(input): # Roll all round rocks (O) as far north as possible
    output = input
    freeSpace = [0] * len(input[0])
    for row in range(len(output)):
        for col in range (len(output[0])):
            if output[row][col] == '#': # Square rock, next free space is below it
                freeSpace[col] = row+1
            if output[row][col] == 'O':
                if row == 0 or output[row-1][col] != '.': # Can't move up
                    freeSpace[col] = row+1
                else: # Move up
                    output[row][col] = '.'
                    output[freeSpace[col]][col] = 'O'
                    freeSpace[col] += 1

    return output

def rollSouth(input):
    output = rollNorth(np.flipud(input).tolist())
    output = np.flipud(output).tolist()
    return output

def rollEast(input):
    output = rollNorth(np.rot90(input).tolist())
    output = np.rot90(output, 3).tolist()
    return output

def rollWest(input):
    output = rollNorth(np.rot90(input, 3).tolist())
    output = np.rot90(output).tolist()
    return output

def spinCycle(input): #Tilt rocks North, West, South, East
    output = rollNorth(input)
    output = rollWest(output)
    output = rollSouth(output)
    output = rollEast(output)
    return output


def calcScore(input):
    score = 0
    for row in range(len(input)):
        score += input[row].count('O') * (len(input) - row)
        #print(score)
    return score

# printField(newField)

def fieldToTuple(field):
    return tuple(tuple(row) for row in field)


maxCycles = 1000000000
seenFields = {fieldToTuple(field)}
foundField = None
newField = field
found = -1
for i in range(1, maxCycles+1):
    newField = spinCycle(newField)
    #printField(newField)
    fieldTuple = fieldToTuple(newField)
    if found == -1:
        if fieldTuple in seenFields:
            printField(newField)
            foundField = fieldTuple
            found = i
            print("Match found after", i, "cycles")
    else:
        if fieldTuple == foundField:
            print("Cycle length:", i - found)
            printField(newField)
            break
    seenFields.add(fieldTuple)

target = (maxCycles - found) % (i - found)
print("Target:", target)

for i in range(target):
    newField = spinCycle(newField)

print(calcScore(newField))
