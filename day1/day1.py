def part1():
    with open('input.txt', 'r') as file:
        text = file.read()

    elves = [sum([int(i) if i != '' else 0 for i in nums.split('\n')]) for nums in text.split('\n\n')]
    print(max(elves))


def part2():
    with open('input.txt', 'r') as file:
        text = file.read()

    elves = [sum([int(i) if i != '' else 0 for i in nums.split('\n')]) for nums in text.split('\n\n')]
    elves.sort(reverse=True)
    print(sum(elves[0:3]))


if __name__ == '__main__':
    part1()
    part2()
