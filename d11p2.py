import numpy as np
f = open("d11_input.txt", "r")

# Make sure the list doesn't wrap around and read a symbol from bottom for top, for example
lines = f.read().splitlines()

# Add rows
expansion_lines = []
for i in range(len(lines)):
    empty = True
    for c in lines[i]:
        if c == '#':
            empty = False
            break

    if empty:
        expansion_lines.append(i)

for i in reversed(expansion_lines):  # Reversed so index of later lines is unaffected by earlier expansions
    lines.insert(i, 'M' * len(lines[i]))

print("Basic lines (Rows added)")
for line in lines:
    print(line)


# Add columns
listed_lines = [list(line) for line in lines]
transposed = np.array(listed_lines).T.tolist()

# Same as before, but adding rows to transposed list means adding columns
expansion_lines = []
for i in range(len(transposed)):
    empty = True
    for c in transposed[i]:
        if c == '#':
            empty = False
            break

    if empty:
        expansion_lines.append(i)

for i in reversed(expansion_lines):  # Reversed so index of later lines is unaffected by earlier expansions
    transposed.insert(i, ['M'] * len(transposed[i]))

final_lines = np.array(transposed).T.tolist()

print("Added columns:")
for line in final_lines:
    print(line)

result = 0
galaxies = []
# Add all galaxies to list as [i,j]
for i in range(len(final_lines)):
    for j in range(len(final_lines[i])):
        if final_lines[i][j] == '#':
            galaxies.append([i,j])

#print("Galaxies: " + str(galaxies))

# How many lines each added line counts as
factor = 999999
# Add shortest path to result for all galaxies further in list
for i in range(len(galaxies) - 1):
    for j in range(i+1, len(galaxies)):
        #result += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
        # Go horizontal, 2nd galaxy is first because range is start inclusive end exclusive
        step = 1
        if galaxies[j][1] > galaxies[i][1]: step = -1  # Go backwards if you need to
        for k in range(galaxies[j][1], galaxies[i][1], step):
            # Use galaxy 1's row, k as column
            if final_lines[galaxies[i][0]][k] == 'M':
                result += factor
            else:
                result += 1
            #final_lines[galaxies[i][0]][k] = 'X'
        # Now go vertical along 2nd galaxy's column
        #print(result)
        step = 1
        if galaxies[i][0] > galaxies[j][0]: step = -1  # Go backwards if you need to
        for k in range(galaxies[i][0]+step, galaxies[j][0]+step, step):
            # Use galaxy 2's col, k as row
            if final_lines[k][galaxies[j][1]] == 'M':
                result += factor
            else:
                result += 1
            #final_lines[k][galaxies[j][1]] = 'Y'


print("Result: " + str(result))

for line in final_lines:
    #print(line)
    continue
