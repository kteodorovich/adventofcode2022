def part1():
    stacks = [['Q', 'F', 'M', 'R', 'L', 'W', 'C', 'V'],
              ['D', 'Q', 'L'],
              ['P', 'S', 'R', 'G', 'W', 'C', 'N', 'B'],
              ['L', 'C', 'D', 'H', 'B', 'Q', 'G'],
              ['V', 'G', 'L', 'F', 'Z', 'S'],
              ['D', 'G', 'N', 'P'],
              ['D', 'Z', 'P', 'V', 'F', 'C', 'W'],
              ['C', 'P', 'D', 'M', 'S'],
              ['Z', 'N', 'W', 'T', 'V', 'M', 'P', 'C']]

    with open('input.txt', 'r') as f:
        for line in f.readlines()[10:]:
            data = line.strip().split(' ')
            num = int(data[1])
            start = int(data[3]) - 1
            end = int(data[5]) - 1

            for i in range(num):
                stacks[end].append(stacks[start].pop(-1))

    print(''.join([stack[-1] for stack in stacks]))


def part2():
    stacks = [['Q', 'F', 'M', 'R', 'L', 'W', 'C', 'V'],
              ['D', 'Q', 'L'],
              ['P', 'S', 'R', 'G', 'W', 'C', 'N', 'B'],
              ['L', 'C', 'D', 'H', 'B', 'Q', 'G'],
              ['V', 'G', 'L', 'F', 'Z', 'S'],
              ['D', 'G', 'N', 'P'],
              ['D', 'Z', 'P', 'V', 'F', 'C', 'W'],
              ['C', 'P', 'D', 'M', 'S'],
              ['Z', 'N', 'W', 'T', 'V', 'M', 'P', 'C']]

    with open('input.txt', 'r') as f:
        for line in f.readlines()[10:]:
            data = line.strip().split(' ')
            num = int(data[1])
            start = int(data[3]) - 1
            end = int(data[5]) - 1

            stacks[end] += stacks[start][-num:]
            stacks[start] = stacks[start][:-num]

    print(''.join([stack[-1] for stack in stacks]))


if __name__ == '__main__':
    part1()
    part2()
