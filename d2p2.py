import re

f = open("d2_input.txt", "r")
result = 0
red_pattern = r"\b(\d+) red"
green_pattern = r"\b(\d+) green"
blue_pattern = r"\b(\d+) blue"

for line in f:
    max_red, max_green, max_blue = 0, 0, 0
    for num in re.findall(red_pattern, line):
        if int(num) > max_red:
            max_red = int(num)
    for num in re.findall(green_pattern, line):
        if int(num) > max_green:
            max_green = int(num)
    for num in re.findall(blue_pattern, line):
        if int(num) > max_blue:
            max_blue = int(num)

    result += max_blue * max_red * max_green

print(result)
