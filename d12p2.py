import time, functools

f = open("d12_input.txt", "r")
start_time = time.time()



# Feed in input with desired character at front, base case is when string is empty
@functools.cache
def travel(input, target, group, run):
    if not input:
        if (run == 0 and group == len(target)) or (run == target[group] and group == len(target)-1):
            # Success!
            return 1
        return 0
    if input[0] == '#':  # Check first character, see if it's ok to be a #
        if group >= len(target):
            return 0
        run += 1
        if run > target[group]: #Too many # in a row for current run
            return 0
        return travel(input[1:], target, group, run)
    elif input[0] == '.':
        if group < len(target):
            if target[group] != run and run > 0:
                return 0
        if run != 0:
            group += 1
            if group > len(target): return 0
            run = 0
        return travel(input[1:], target, group, run)
    else:
        return travel('.' + input[1:], target, group, run) + travel('#' + input[1:], target, group, run)

total = 0
for line in f.readlines():
    input = line.strip().split(' ')
    base = input[0]
    for i in range(0,4):
        input[0] += '?' + base
    target = tuple(map(int, input[1].split(','))) * 5
    #print(input[0])
    #print(target)
    total += travel(input[0], target, 0, 0)


print("Total: " + str(total) + " done in " + str(time.time() - start_time))