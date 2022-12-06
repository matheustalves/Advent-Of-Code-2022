line = open('6.txt').read().rstrip()


def marker(size: int) -> int:
    for i in range(size, len(line)):

        if len(set(line[i - size: i])) == size:
            return i

    return None


print(f'Part 1 Result: {marker(4)}')
print(f'Part 2 Result: {marker(14)}')
