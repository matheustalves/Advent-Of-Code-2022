part1 = part2 = 0

with open('4.txt') as f:
    while True:
        line = f.readline().rstrip()
        if not line:
            break

        line = line.split(',')

        left = tuple(int(item) for item in line[0].split('-'))
        right = tuple(int(item) for item in line[1].split('-'))

        if (left[0] <= right[0] and left[1] >= right[1]) or (right[0] <= left[0] and right[1] >= left[1]):
            part1 += 1

        if not (left[0] < right[0] and left[1] < right[0]) and not (right[0] < left[0] and right[1] < left[0]):
            part2 += 1


print(f'Part 1 result: {part1}')
print(f'Part 2 result: {part2}')
