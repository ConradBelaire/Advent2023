import re
f = open("d5_input.txt", "r")

# Make sure the list doesn't wrap around and read a symbol from bottom for top, for example
lines = f.readlines()
num_pattern = r"(?!=\d)(\d+)(?!\d)"
result = 999999999

# Break input into chunks
chunks = []
curr = []
for line in lines:
    if line == "\n":
        chunks.append(curr)
        curr = []
        continue
    curr.append(line.strip())
chunks.append(curr)
# print(chunks)

# Create list of dictionaries
conversions = []
for chunk in chunks[1:]:
    d = {}
    for line in chunk[1:]:
        nums = list(map(int, re.findall(num_pattern, line)))
        d[(nums[1], nums[1] + nums[2])] = nums[0]
    conversions.append(d)
# print(conversions)

seeds = list(map(int, re.findall(num_pattern, chunks[0][0])))
for seed in seeds:
    for d in conversions:
        for k in d.keys():
            if seed >= k[0] and seed < k[1]:
                # print(seed, k[0], k[1], d[k] + seed - k[0])
                seed = d[k] + seed - k[0]
                break
    result = min(result, seed)

print(result)