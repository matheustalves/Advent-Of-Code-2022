files = {}
folders = set()
cur = []

with open('7.txt') as f:
    while True:
        line = f.readline().rstrip()
        if not line:
            break

        line = line.split(' ')

        match line:
            case ['$', 'cd', '..']:
                if len(cur) > 0:
                    cur.pop()

            case ['$', 'cd', '/']:
                cur = []

            case ['$', 'cd', name]:
                cur.extend(name.split('/'))

            case [size, name] if size.isnumeric():
                files['/'.join(cur + [name])] = int(size)

        folders.add('/'.join(cur))


part1 = 0
sizes = {}
for folder in folders:
    size = 0

    for file in files:
        if file.startswith(folder):
            size += files[file]

    if size <= 100000:
        part1 += size

    sizes[folder] = size

print(f'Part 1 Result: {part1}')
print(
    f'Part 2 Result: {min(size for size in sizes.values() if 70000000 - sizes[""] + size >= 30000000)}')
