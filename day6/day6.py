def part1():
    with open('input.txt', 'r') as f:
        text = f.read()
    for i in range(len(text)):
        if len(set(text[i:i + 4])) == 4:
            print(i + 4)
            break

    # one liner lol
    # print([1 if i > 2 and len(set(text[i - 4:i])) == 4 else 0 for i in range(len(text))].index(1))


def part2():
    with open('input.txt', 'r') as f:
        text = f.read()
    for i in range(len(text)):
        if len(set(text[i:i + 14])) == 14:
            print(i + 14)
            break


if __name__ == '__main__':
    part1()
    part2()
