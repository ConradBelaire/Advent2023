

f = open("d16_input.txt", "r")
lines = f.read().splitlines()

print(lines)

energized = [[0] * len(lines[0]) for _ in range(len(lines))]
# Flag key: 1111 = up down left right
# up = & 8
# down = & 4
# left = & 2
# right = & 1

# move(row, col) is the new position. It checks if there's a problem at the start of the func, and immediately returns if so

moveQueue = [] # (row, col, dir)

def move(row, col, dir):
    if (col) < 0 or (col) >= len(lines[0]) or (row) < 0 or (row) >= len(lines): # If going out of the map
        return
    if energized[row][col] & dir != 0: # Already visited square from this direction
        return
    energized[row][col] += dir # Energized, and marks that it's visited from this direction
    
    c = lines[row][col]
    if dir == 8: # up
        if c == '.' or c == '|':
            moveQueue.append((row - 1, col, 8)) # up
            return
        if c == '-':
            moveQueue.append((row, col - 1, 2)) # left
            moveQueue.append((row, col + 1, 1)) # right
            return
        if c == '/':
            moveQueue.append((row, col + 1, 1)) # right
            return
        if c == '\\':
            moveQueue.append((row, col - 1, 2)) # left
            return
    if dir == 4: # down
        if c == '.' or c == '|':
            moveQueue.append((row + 1, col, 4)) # down
            return
        if c == '-':
            moveQueue.append((row, col - 1, 2)) # left
            moveQueue.append((row, col + 1, 1)) # right
            return
        if c == '/':
            moveQueue.append((row, col - 1, 2)) # left
            return
        if c == '\\':
            moveQueue.append((row, col + 1, 1)) # right
            return
    if dir == 2: # left
        if c == '.' or c == '-':
            moveQueue.append((row, col - 1, 2)) # left
            return
        if c == '|':
            moveQueue.append((row - 1, col, 8)) # up
            moveQueue.append((row + 1, col, 4)) # down
            return
        if c == '/':
            moveQueue.append((row + 1, col, 4)) # down
            return
        if c == '\\':
            moveQueue.append((row - 1, col, 8)) # up
            return
    if dir == 1: # right
        if c == '.' or c == '-':
            moveQueue.append((row, col + 1, 1)) # right
            return
        if c == '|':
            moveQueue.append((row - 1, col, 8)) # up
            moveQueue.append((row + 1, col, 4)) # down
            return
        if c == '/':
            moveQueue.append((row - 1, col, 8)) # up
            return
        if c == '\\':
            moveQueue.append((row + 1, col, 4)) # down
            return

# Start at top left corner, going right
move(0, 0, 1)
while len(moveQueue) > 0:
    pos = moveQueue.pop(0)
    move(pos[0], pos[1], pos[2])

def printField(input):
    for row in input:
        print(' '.join(map(str, row)))
    print()

printField(energized)

total = 0
for row in range(len(energized)):
    for col in range(len(energized[0])):
        if energized[row][col] != 0:
            total += 1
print(total)
