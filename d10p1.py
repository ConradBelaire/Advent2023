
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

# Find S
for i in range(len(lines)):
    spot = lines[i].find('S')
    if spot != -1:
        position = [i, spot]

print(position)
# Travel pipes
longest = 0
# Go south
facing = 's'
while True:
    longest += 1
    offset = direction_dict[facing]
    c = lines[position[0] + offset[0]][position[1] + offset[1]]

    if c == 'S': break
    #This is: get inverse of current facing (since we're coming from that direction), subtract it from the pipe_dict
    #of our next pipe, and update our facing. This way, whichever way we come from, we ignore, and take the other facing
    facing = list(set(pipe_dict[c]) - {inverse_dict[facing]})[0]
    position = [position[0] + offset[0], position[1] + offset[1]]

result = longest // 2 + (longest % 2)

print(result)
