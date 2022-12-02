part1 = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,

    'B X': 1,
    'B Y': 5,
    'B Z': 9,

    'C X': 7,
    'C Y': 2,
    'C Z': 6,
}

part2 = {
    'A X': 3,
    'A Y': 4,
    'A Z': 8,

    'B X': 1,
    'B Y': 5,
    'B Z': 9,

    'C X': 2,
    'C Y': 6,
    'C Z': 7,
}

total1 = total2 = 0

with open('2.txt') as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        total1 += part1[line]
        total2 += part2[line]

print(total1)
print(total2)
