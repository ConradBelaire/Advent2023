f = open("d9_input.txt", "r")

# Make sure the list doesn't wrap around and read a symbol from bottom for top, for example
lines = f.readlines()
result = 0

for line in lines:
    numbers = [list(map(int, line.split()))]

    # Build the triangle
    zeroes = True
    while True:
        if all(num == 0 for num in numbers[-1]): break
        numbers.append([])
        for i in range(len(numbers[-2]) - 1):
            numbers[-1].append(numbers[-2][i+1] - numbers[-2][i])
            # print(numbers)

    print(numbers)
    # Traverse upwards
    numbers[-1].append(0)
    for i in range(len(numbers)-2, -1, -1):
        numbers[i].append(numbers[i][-1] + numbers[i+1][-1])
    # print(numbers)
    result += numbers[0][-1]
print(result)
