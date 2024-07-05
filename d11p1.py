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
    lines.insert(i, lines[i])

#print("Basic lines (Rows added)")
#for line in lines:
    #print(line)


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
    transposed.insert(i, transposed[i])

final_lines = np.array(transposed).T.tolist()

#print("Added columns:")
#for line in final_lines:
    #print(line)

result = 0
galaxies = []
# Add all galaxies to list as [i,j]
for i in range(len(final_lines)):
    for j in range(len(final_lines[i])):
        if final_lines[i][j] == '#':
            galaxies.append([i,j])

#print("Galaxies: " + str(galaxies))

# Add shortest path to result for all galaxies further in list
for i in range(len(galaxies) - 1):
    for j in range(i+1, len(galaxies)):
        result += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])

print("Result: " + str(result))
