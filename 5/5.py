stacks, moves = [], []

with open('5.txt') as f:
    while True:
        line = f.readline()
        if not line:
            break

        line = line.rstrip()

        if '[' in line:  # creates stacks
            for i in range(1, len(line), 4):
                element = line[i]

                index = i // 4
                while len(stacks) < index + 1:
                    stacks.append([])

                if element != ' ':
                    stacks[index].append(element)

        else:  # creates moves
            line = line.split()
            if 'move' in line:
                moves.append([int(num) for num in line if num.isdigit()])


stacks2 = stacks.copy()

for move in moves:
    qnt = move[0]
    from_index = move[1] - 1
    to_index = move[2] - 1

    # Part 1
    stacks[to_index] = list(
        reversed(stacks[from_index][:qnt])) + stacks[to_index]
    stacks[from_index] = stacks[from_index][qnt:]

    # Part 2
    stacks2[to_index] = stacks2[from_index][:qnt] + stacks2[to_index]
    stacks2[from_index] = stacks2[from_index][qnt:]


print('Part 1 Result: ' + ''.join([stack[0]
      for stack in stacks if len(stacks) > 0]))
print('Part 2 Result: ' + ''.join([stack[0]
      for stack in stacks2 if len(stacks2) > 0]))
