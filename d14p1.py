

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
#printField(field)

def rollNorth(input):
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

#printField(rollNorth(field))

def calcScore(input):
    score = 0
    for row in range(len(input)):
        score += input[row].count('O') * (len(input) - row)
        #print(score)
    return score

print(calcScore(rollNorth(field)))
