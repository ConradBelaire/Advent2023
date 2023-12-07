import re

f = open("d5_input.txt", "r")

lines = f.readlines()
num_pattern = r"(?!=\d)(\d+)(?!\d)"

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

s_input = list(map(int, re.findall(num_pattern, chunks[0][0])))
seed_pairs = []
for (i, k) in zip(s_input[0::2], s_input[1::2]):
    seed_pairs.append((i, i+k))
print(seed_pairs)


def travel(front, back, dict_depth=0):
    if dict_depth == len(conversions):
        return [front]
    conv = conversions[dict_depth]
    for k in conv.keys():
        if k[0] <= front <= back <= k[1]:
            front = conv[k] + front - k[0]
            back = conv[k] + back - k[0]
            return travel(front, back, dict_depth + 1)
        if k[0] <= front < k[1] < back:
            middle = k[1]
            return (travel(conv[k] + front - k[0], conv[k] + middle - k[0], dict_depth + 1)
                    + travel(middle, back, dict_depth))
        if front <= k[0] < back < k[1]:
            middle = k[0]
            return (travel(front, middle, dict_depth)
                    + travel(conv[k] + middle - k[0], conv[k] + back - k[0], dict_depth + 1))

    return travel(front, back, dict_depth + 1)


results = []
for pair in seed_pairs:
    results += travel(pair[0], pair[1])
print(results)
print(min(results))

