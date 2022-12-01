sums = []

with open('1.txt') as f:
    lines = f.readlines()
    s = 0
    for line in lines:
        if line != '\n':
            s += int(line)
        else:
            sums.append(s)
            s = 0

sums.sort()

print(sums[-1])  # part 1
print(sums[-1] + sums[-2] + sums[-3])  # part2
