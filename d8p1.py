import re
f = open("d8_input.txt", "r")

# Make sure the list doesn't wrap around and read a symbol from bottom for top, for example
lines = f.readlines()
directions = re.findall(r"\w", lines[0])
nodes = {}
result = 0
node_pattern = r"(\w+) = \((\w+), (\w+)\)"

for line in lines[2:]:
    items = re.search(node_pattern, line)
    nodes[items.group(1)] = [items.group(2), items.group(3)]

position = "AAA"
d_index = 0
while position != "ZZZ":
    if directions[d_index] == 'L':
        position = nodes[position][0]
    else:
        position = nodes[position][1]
    d_index += 1
    if d_index >= len(directions): d_index = 0
    result += 1

print(nodes)
print(result)
