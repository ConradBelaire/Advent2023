import re
f = open("d4_input.txt", "r")

# Make sure the list doesn't wrap around and read a symbol from bottom for top, for example
lines = f.readlines()
num_pattern = r"(?!=\d)(\d+)(?!\d)"
result = 0
copies = [1] * len(lines)

for i in range(len(lines)):
    score = 0
    line = lines[i].split(":")[1]
    winners = list(map(int, re.findall(num_pattern, line.split("|")[0])))
    nums = list(map(int, re.findall(num_pattern, line.split("|")[1])))
    for num in nums:
        if num in winners:
            score += 1
    for j in range(score):
        if i + j + 1 > len(lines): break
        copies[i+j+1] += copies[i]
    result += copies[i]
    print(winners, nums, score)

print(result)
