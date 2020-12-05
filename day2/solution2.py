def part1():
    with open('input.txt') as infile:
        ctr = 0

        for line in infile:
            line = line.strip().split(' ')
            lower, upper = map(int, line[0].split('-'))
            char = line[1].strip(':')
            cnt = line[-1].count(char)

            if lower <= cnt and cnt <= upper:
                ctr += 1

    return ctr

def part2():
    with open('input.txt') as infile:
        ctr = 0

        for line in infile:
            line = line.strip().split(' ')
            idx1, idx2 = map(lambda x: int(x) - 1, line[0].split('-'))
            char = line[1].strip(':')

            if (line[-1][idx1] == char and line[-1][idx2] != char) or \
               (line[-1][idx1] != char and line[-1][idx2] == char):
                ctr += 1

    return ctr

if __name__ == '__main__':
    print('valid passwords under policy 1:', part1())
    print('valid passwords under policy 2:', part2())
