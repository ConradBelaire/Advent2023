

f = open("d15_input.txt", "r")
line = f.readline().strip().split(',')

def hashFunc(s):
    result = 0
    for c in s:
        result += ord(c)
        result *= 17
        result %= 256
    return result

total = 0
for s in line:
    total += hashFunc(s)
print(total)
