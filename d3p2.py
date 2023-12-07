import re
f = open("d3_input.txt", "r")

# Make sure the list doesn't wrap around and read a symbol from bottom for top, for example
lines = f.readlines()
lines.insert(0, "." * len(lines[0]))
lines.append("." * len(lines[0]))

result = 0
num_pattern = r"(?!=\d)(\d+)(?!\d)"
gear_dict = {}

for i in range(len(lines)):
    line = lines[i]
    numbers = re.finditer(num_pattern, line)

    for match in numbers:
        front, back = match.span()[0], match.span()[1]
        # print(front, back, match.group(1))
        for x in range(i-1, i+2):
            for y in range(max(front-1, 0), min(back+1, len(lines))):
                if lines[x][y] == '*':
                    gear_dict.setdefault((x, y), []).append(int(match.group(1)))


# print(gear_dict)
for key in gear_dict:
    if len(gear_dict[key]) == 2:
        result += gear_dict[key][0] * gear_dict[key][1]
print(result)
