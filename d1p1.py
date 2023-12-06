f = open("d1p1_input.txt", "r")
result = 0
for line in f:
    current = 0
    for c in line:
        if c.isnumeric():
            current = 10 * int(c)
            break
    for c in reversed(line):
        if c.isnumeric():
            current += int(c)
            break
    result += current

print(result)
