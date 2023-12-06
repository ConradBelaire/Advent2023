f = open("d1p1_input.txt", "r")

numDict = {'0' : 0,
           'zero' : 0,
           '1' : 1,
           'one' : 1,
           '2' : 2,
           'two' : 2,
           '3' : 3,
           'three' : 3,
           '4' : 4,
           'four' : 4,
           '5' : 5,
           'five' : 5,
           '6' : 6,
           'six' : 6,
           '7' : 7,
           'seven' : 7,
           '8' : 8,
           'eight' : 8,
           '9' : 9,
           'nine' : 9}
result = 0
for line in f:
    current = 0
    # Forwards
    for i in range(len(line)):
        if line[i:i+1] in numDict.keys(): #check for length 1 matches
            current = 10 * numDict[line[i:i+1]]
            break
        if line[i:i+3] in numDict.keys(): #check for length 3 matches
            current = 10 * numDict[line[i:i+3]]
            break
        if line[i:i+4] in numDict.keys(): #check for length 4 matches
            current = 10 * numDict[line[i:i+4]]
            break
        if line[i:i+5] in numDict.keys(): #check for length 5 matches
            current = 10 * numDict[line[i:i+5]]
            break

    # Backwards
    for i in range(len(line), 0, -1):
        if line[i-1:i] in numDict.keys(): #check for length 1 matches
            current += numDict[line[i-1:i]]
            break
        if line[i-3:i] in numDict.keys(): #check for length 3 matches
            current += numDict[line[i-3:i]]
            break
        if line[i-4:i] in numDict.keys(): #check for length 4 matches
            current += numDict[line[i-4:i]]
            break
        if line[i-5:i] in numDict.keys(): #check for length 5 matches
            current += numDict[line[i-5:i]]
            break

    result += current

print(result)
