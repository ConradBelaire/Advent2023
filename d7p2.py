import re
import math
f = open("d7_input.txt", "r")

# Make sure the list doesn't wrap around and read a symbol from bottom for top, for example
lines = f.readlines()
hands = []  # [hand, bet, hand type (pair, 2 pair, etc)]
result = 0


for line in lines:
    line = line.strip()
    hands.append([line.split(" ")[0], int(line.split(" ")[1]), 0])

for hand in hands:
    card_count = {}
    for c in hand[0]:
        card_count.setdefault(c, 0)
        card_count[c] += 1
    card_count.setdefault('J', 0)
    j = card_count.pop('J')  # Removes J from the dictionary
    card_count.setdefault('J', 0)  # Covers edge case of 5 J

    if max(card_count.values()) + j == 1:
        hand[2] = 1
    elif max(card_count.values()) + j == 2:
        if j == 0:
            if list(card_count.values()).count(2) == 2:
                hand[2] = 3
            else:
                hand[2] = 2
        else:  # j must be 1, and no regular matches. Therefore, only a single pair is possible.
            hand[2] = 2

    elif max(card_count.values()) + j == 3:
        if j == 0:
            if list(card_count.values()).count(2) == 1:
                hand[2] = 5
            else:
                hand[2] = 4
        elif j == 1:
            if list(card_count.values()).count(2) == 2:
                hand[2] = 5
            else:
                hand[2] = 4
        else:  # 2 j, max count is 1. Only three of a kind
            hand[2] = 4
    elif max(card_count.values()) + j == 4:
        hand[2] = 6
    elif max(card_count.values()) + j == 5:
        hand[2] = 7

def highCardSort(h):
    output = 0
    for i in range(5):
        x = h[0][i]

        if x == 'A': output += 14 * pow(10, 10-2*i)
        elif x == 'K': output += 13 * pow(10, 10-2*i)
        elif x == 'Q': output += 12 * pow(10, 10-2*i)
        elif x == 'J': output += 1 * pow(10, 10-2*i)
        elif x == 'T': output += 10 * pow(10, 10-2*i)
        else: output += int(x) * pow(10, 10-2*i)
    return output


# Worst first. First sorts by high card, then by hand score.
hands.sort(key=highCardSort)
hands.sort(key=lambda x: x[2])

for i in range(len(hands)):
    result += hands[i][1] * (i+1)

print(hands)

print(result)
