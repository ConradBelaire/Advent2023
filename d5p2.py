import re

f = open("d5_input.txt", "r")

# Make sure the list doesn't wrap around and read a symbol from bottom for top, for example
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
            # print("within bounds:", front, back, k)
            front = conv[k] + front - k[0]
            back = conv[k] + back - k[0]
            return travel(front, back, dict_depth + 1)
        if k[0] <= front < k[1] < back:
            middle = k[1]
            # if conv[k] + front - k[0] == 0:
                # ("Front Zero!", front, back, k, conv[k] + front - k[0], dict_depth)
            # print("front intersect:", front, back, k)
            return (travel(conv[k] + front - k[0], conv[k] + middle - k[0], dict_depth + 1)
                    + travel(middle, back, dict_depth))
        if front < k[0] <= back < k[1]:
            # print("back intersect:", front, back, k)
            middle = k[1]
            if conv[k] + middle - k[0] == 0:
                print("Back Zero!", front, back, k, conv[k] + middle - k[0], dict_depth)
            return (travel(front, middle, dict_depth)
                    + travel(conv[k] + middle - k[0], conv[k] + back - k[0], dict_depth + 1))

    # print("no bounds:", front, back, conv.keys())
    return travel(front, back, dict_depth + 1)


results = []
for pair in seed_pairs:
    results += travel(pair[0], pair[1])
print(results)
print(min(results))


# HELL ZONE
# Create list of dictionaries
reverse_conversions = []
for chunk in chunks[1:]:
    d = {}
    for line in chunk[1:]:
        nums = list(map(int, re.findall(num_pattern, line)))
        d[(nums[0], nums[0] + nums[2])] = nums[1]
    reverse_conversions.insert(0, d)

seed = 3869686154
for d in reverse_conversions:
    for k in d.keys():
        # print(seed, k)
        if k[0] <= seed < k[1]:
            # print(seed, k[0], k[1], d[k] + seed - k[0])
            seed = d[k] + seed - k[0]
# print(seed)
