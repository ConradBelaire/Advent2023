import re, itertools
f = open("d12_input.txt", "r")

total = 0
for line in f.readlines():
    input = line.strip().split(' ')
    #print("Beginning line: " + line.strip())
    #matches = re.findall(r"#+", input[0])
    target = []
    for n in list(map(int, input[1].split(','))):
        target.append('#' * n)
    chunks = re.split(r"\?", input[0])
    #print(chunks)

    iterations = itertools.product(('.', '#'), repeat=len(chunks) - 1)
    for i in iterations:
        output = chunks[0]
        for j in range(0, len(chunks) - 1):  # Skip first chunk
            output += i[j] + chunks[j + 1]
        #print("Testing case: " + output)
        matches = re.findall(r"#+", output)
        if matches == target:
            total += 1
            #print("Match found!")

print("Total: " + str(total))