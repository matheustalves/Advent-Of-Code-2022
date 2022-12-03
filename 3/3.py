def part1() -> int:
    total = 0

    with open('3.txt') as f:
        while True:
            line = f.readline().rstrip()
            if not line:
                break

            left = set(line[:len(line) // 2])
            right = set(line[len(line) // 2:])

            for item in left:
                if item in right:
                    if item <= 'Z':
                        total += ord(item) - 38
                    else:
                        total += ord(item) - 96

    return total


def part2() -> int:
    total = 0

    with open('3.txt') as f:
        i = 0
        arr = ['', '', '']

        while True:
            line = f.readline().rstrip()
            if not line:
                break

            if i < 2:
                arr[i] = set(line)
                i += 1
                continue

            arr[i] = set(line)
            i = 0

            for item in arr[0]:
                if item in arr[1] and item in arr[2]:
                    if item <= 'Z':
                        total += ord(item) - 38
                    else:
                        total += ord(item) - 96

    return total


if __name__ == '__main__':
    print(part1())
    print(part2())
