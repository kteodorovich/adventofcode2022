def part1():
    count = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            split = line.split(',')
            r1 = tuple(map(int, split[0].split('-')))
            r2 = tuple(map(int, split[1].split('-')))

            if (r1[0] >= r2[0] and r1[1] <= r2[1]) or (r2[0] >= r1[0] and r2[1] <= r1[1]):
                count += 1

    print(count)


def part2():
    count = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            split = line.split(',')
            r1 = tuple(map(int, split[0].split('-')))
            r2 = tuple(map(int, split[1].split('-')))

            if r2[0] <= r1[0] <= r2[1] or r1[0] <= r2[0] <= r1[1]:
                count += 1

    print(count)


if __name__ == '__main__':
    part1()
    part2()
