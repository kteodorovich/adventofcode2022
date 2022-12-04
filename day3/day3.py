def part1():
    priority = 0
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            bag1 = line[:len(line) // 2].strip()
            bag2 = line[len(line) // 2:].strip()

            for char in bag1:
                if char in bag2:
                    bag2 = bag2.replace(char, '')

                    priority += ord(char) - 96 if ord(char) > 96 else ord(char) - 38

    print(priority)


def part2():
    priority = 0

    with open('input.txt', 'r') as f:
        lines = f.readlines()
    for i in range(0, len(lines), 3):
        bag1 = lines[i].strip()
        bag2 = lines[i + 1].strip()
        bag3 = lines[i + 2].strip()

        for char in bag1:
            if char in bag2 and char in bag3:
                bag2 = bag2.replace(char, '')
                bag3 = bag3.replace(char, '')

                priority += ord(char) - 96 if ord(char) > 96 else ord(char) - 38

    print(priority)


if __name__ == '__main__':
    part1()
    part2()
