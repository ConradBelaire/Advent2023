
f = open("d10_input.txt", "r")

# Make sure the list doesn't wrap around and read a symbol from bottom for top, for example
lines = f.readlines()
result = 0
pipe_dict = {
    '|': ['n', 's'],
    '-': ['w', 'e'],
    'L': ['n', 'e'],
    'J': ['n', 'w'],
    '7': ['s', 'w'],
    'F': ['s', 'e']
}
direction_dict = {
    'n': [-1, 0],
    's': [1, 0],
    'w': [0, -1],
    'e': [0, 1]
}
inverse_dict = {
    'n': 's',
    's': 'n',
    'w': 'e',
    'e': 'w',
}
position = []
visited = []  # This will hold positions [y,x] of each pipe we travel in the main path

# Find S
for i in range(len(lines)):
    spot = lines[i].find('S')
    if spot != -1:
        position = [i, spot]
        break

print(position)
visited.append(position)
# Travel pipes
longest = 0
# Go south. This is kind of cheating but all inputs have south as one of the options.
facing = 's'
while True:
    #longest += 1
    offset = direction_dict[facing]
    c = lines[position[0] + offset[0]][position[1] + offset[1]]

    if c == 'S': break
    #This is: get inverse of current facing (since we're coming from that direction), subtract it from the pipe_dict
    #of our next pipe, and update our facing. This way, whichever way we come from, we ignore, and take the other facing
    facing = list(set(pipe_dict[c]) - {inverse_dict[facing]})[0]
    position = [position[0] + offset[0], position[1] + offset[1]]
    visited.append(position)

#print(visited)

# Now we have a list of all positions that are in the main loop
# As we traverse: if we find main piece that's a |, we switch
# If we find a main piece that's an elbow, hold onto that info, and keep looking right
# Keep going until we find another elbow. If it matches first elbow, don't switch
# If it is opposite of first elbow, switch
#print(facing)
last_elbow = ""
counting = False
for y in range(len(lines)):
    line = lines[y]
    for x in range(len(line)):

        if line[x] == 'S':  # Convert S into its true form
            if facing == 'w':
                line = line.replace('S', 'F')
            else:
                line = line.replace('S', '7')
            print(line)

        if [y,x] in visited:
            if line[x] == '-':
                continue
            elif line[x] == 'J':
                if last_elbow == "L":
                    last_elbow = ""
                else:
                    counting = not counting
                    #print("Swap: [", x, ",", y, "]: ", line[x])
            elif line[x] == '7':
                if last_elbow == "F":
                    last_elbow = ""
                else:
                    counting = not counting
                    #print("Swap: [", x, ",", y, "]: ", line[x])
            elif line[x] == '|':
                counting = not counting
                #print("Swap: [", x, ",", y, "]: ", line[x])
            else:
                last_elbow = line[x]

        else:
            if counting:
                #print("Count: [", x, ",", y, "]: ", line[x])
                result += 1




print(result)
