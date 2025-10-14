import numpy as np
f = open("d13_inpute.txt", "r")

eof = False
total = 0

while not eof:
    field = []
    while True:
        line = f.readline()
        if line == "\n":
            break
        if not line:
            eof = True
            break
        field.append(line.strip())
    print(field)
    result = 0
    for i in range(1, len(field)):
        if field[i] == field[i-1]:
            result = i * 100  # Setting this here, will be overwritten if this is a false alarm
            j = 1
            while i + j < len(field) and i - j - 1 >= 0:
                if field[i+j] != field[i-j-1]:  # False alarm, return to for loop
                    result = 0
                    j += 1
                    break

                j += 1
            # If not broken from last loop, we've found our reflection
            if result != 0:
                break
    if result != 0:
        total += result
        continue

    field = list(map(list, field))
    transposed = np.array(field).T.tolist()  # Transpose input so we can reuse last algorithm
    #print(transposed)
    for i in range(1, len(transposed)):
        if transposed[i] == transposed[i-1]:
            result = i  # Setting this here, will be overwritten if this is a false alarm
            j = 1
            while i + j < len(transposed) and i - j - 1 >= 0:
                if transposed[i+j] != transposed[i-j-1]:  # False alarm, return to for loop
                    result = 0
                    j += 1
                    break

                j += 1
            # If not broken from last loop, we've found our reflection
            if result != 0:
                break

    total += result


print(total)
