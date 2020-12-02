def part1():
    with open('input.txt') as infile:
        expenses = [int(line) for line in infile]

    print('part 1:')
    for i, ei in enumerate(expenses):
        for j, ej in enumerate(expenses[i:]):
            if ei + ej == 2020:
                print(f'\t{ei} + {ej} = {ei + ej}')
                print(f'\t{ei} * {ej} = {ei*ej}')

    return

def part2():
    return

if __name__ == '__main__':
    part1()
    part2()
