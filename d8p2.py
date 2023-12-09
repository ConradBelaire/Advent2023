import re
from math import gcd, lcm
from functools import reduce
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

positions = []
results = {}
for k in nodes.keys():
    if k[2] == 'A':
        positions.append(k)
        results[k] = 0
print(positions)

d_index = 0

for position in positions:
    start = position
    while position[2] != "Z":
        if directions[d_index] == 'L':
            position = nodes[position][0]
        else:
            position = nodes[position][1]
        d_index += 1
        if d_index >= len(directions): d_index = 0
        results[start] += 1

result = lcm(*results.values())

print(results)
print(result)
