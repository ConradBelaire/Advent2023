import re

f = open("d2_input.txt", "r")
result = 0
id_pattern = r"^Game (\d+)"
red_pattern = r"\b(\d+) red"
green_pattern = r"\b(\d+) green"
blue_pattern = r"\b(\d+) blue"

for line in f:
    possible = True
    for num in re.findall(red_pattern, line):
        if int(num) > 12:
            possible = False
    for num in re.findall(green_pattern, line):
        if int(num) > 13:
            possible = False
    for num in re.findall(blue_pattern, line):
        if int(num) > 14:
            possible = False
    if possible:
        result += int(re.match(id_pattern, line).group(1))

print(result)
