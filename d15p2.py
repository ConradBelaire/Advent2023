

f = open("d15_input.txt", "r")
line = f.readline().strip().split(',')

def hashFunc(s):
    result = 0
    for c in s:
        if c.isalpha():
            result += ord(c)
            result *= 17
            result %= 256
    return result

boxes = [[] for _ in range(256)]

testBoxes = [[["rn", 1], ["cm", 2]], [], [], [["ot", 7], ["ab", 5], ["pc", 6]]]
def printBoxes(boxes):
    for i in range(len(boxes)):
        if len(boxes[i]) == 0:
            continue
        print(f"Box {i}: ", end='')
        for item in boxes[i]:
            print(f"[{item[0]} {item[1]}] ", end='')
        print()
    print()

def eqFunc(boxes, input):
    box = boxes[hashFunc(input)]
    label = ''.join(char for char in input if char.isalpha())
    num = ''.join(char for char in input if char.isdigit())
    #print(f"Looking for {label} {num} in box {hashFunc(input)}")

    found = False
    for i in range(len(box)):
        if box[i][0] == label:
            found = True
            box[i][1] = num
            #print(f"Updated {label} to {num}")
            break
    if not found:
        box.append([label, num])
        #print(f"Added {label} {num} to box {hashFunc(input)}")

def minFunc(boxes, input):
    box = boxes[hashFunc(input)]
    label = ''.join(char for char in input if char.isalpha())
    #print(f"Removing {label} in box {hashFunc(input)}")

    for i in range(len(box)):
        if box[i][0] == label:
            box.pop(i)
            #print(f"Removed {label}")
            break

for command in line:
    if '=' in command:
        eqFunc(boxes, command)
    elif '-' in command:
        minFunc(boxes, command)

total = 0
for i in range(len(boxes)):
    box = boxes[i]
    for j in range(len(box)):
        total += (1+i) * (1+j) * int(box[j][1])

printBoxes(boxes)
print(total)

