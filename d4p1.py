import re
f = open("d4_input.txt", "r")

# Make sure the list doesn't wrap around and read a symbol from bottom for top, for example
lines = f.readlines()
num_pattern = r"(?!=\d)(\d+)(?!\d)"
result = 0

for line in lines:
    score = 0
    line = line.split(":")[1]
    winners = list(map(int, re.findall(num_pattern, line.split("|")[0])))
    nums = list(map(int, re.findall(num_pattern, line.split("|")[1])))
    for num in nums:
        if num in winners:
            score = max(1, score * 2)
    result += score
    print(winners, nums, score)

print(result)