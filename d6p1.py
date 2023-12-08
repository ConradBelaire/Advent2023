import re
import math
f = open("d6_input.txt", "r")

# Make sure the list doesn't wrap around and read a symbol from bottom for top, for example
lines = f.readlines()
num_pattern = r"(?!=\d)(\d+)(?!\d)"

times = list(map(int, re.findall(num_pattern, lines[0])))
distances = list(map(int, re.findall(num_pattern, lines[1])))
result = 1

for i in range(len(times)):
    mid = math.floor(times[i] / 2)
    points = 0
    print(times[i], distances[i], mid, times[i] - mid)
    if mid == times[i] - mid:
        points = -1
    while mid * (times[i] - mid) > distances[i]:
        points += 2
        mid -= 1

    result *= points
    print("Result for race", i, points)

print(result)
