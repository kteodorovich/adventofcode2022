def part1():
    score = 0

    with open('./input.txt') as f:
        for line in f.readlines():
            move = ord(line[2]) - 87
            opp = ord(line[0]) - 64

            # paper > rock, scissors > paper, rock > scissors
            if (move == 2 and opp == 1) or (move == 3 and opp == 2) or (move == 1 and opp == 3):
                score += 6
            elif move == opp:
                score += 3

            score += move

    print(score)


def part2():
    score = 0

    with open('./input.txt') as f:
        for line in f.readlines():
            outcome = ord(line[2]) - 88
            score += outcome * 3  # add score for lose/draw/win

            opp = ord(line[0]) - 64
            moves = {1: [3, 1, 2], 2: [1, 2, 3], 3: [2, 3, 1]}
            score += moves[opp][outcome]  # add score for rock/paper/scissors

    print(score)


if __name__ == '__main__':
    part1()
    part2()
