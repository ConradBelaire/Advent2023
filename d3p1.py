import re
f = open("d3_input.txt", "r")

# Make sure the list doesn't wrap around and read a symbol from bottom for top, for example
lines = f.readlines()
lines.insert(0, "")
lines.append("")

result = 0
num_pattern = r"(?!=\d)(\d+)(?!\d)"
symbols = ['/', '$', '-', '=', '@', '#', '&', '+', '%', '*']

for i in range(len(lines)):
# for i in [45]:
    line = lines[i]
    # print(re.findall(num_pattern, line))
    numbers = re.finditer(num_pattern, line)
    for match in numbers:
        front, back = match.span()[0], match.span()[1]
        print(front, back, match.group(1), line[front-1], line[back])
        if line[front-1] in symbols or line[back] in symbols:
            result += int(match.group(1))
            continue
        # Need to not double count if multiple symbols found
        # Making it a single string to iterate through, fewer issues with breaking out of for loops
        above_and_below = lines[i-1][front-1:back+1] + lines[i+1][front-1:back+1]
        print(above_and_below)
        for c in above_and_below:
            if c in symbols:
                result += int(match.group(1))
                print(match.group(1), c)
                break

    #How I got list of symbols (manually removed \n)
    #for c in line:
     #   if not c.isnumeric() and c != ".":
      #      all_symbols.append(c)

print(result)