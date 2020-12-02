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
    with open('input.txt') as infile:
        expenses = [int(line) for line in infile]

    print('part 2:')
    for i, ei in enumerate(expenses):
        for j, ej in enumerate(expenses[i:]):
            for k, ek in enumerate(expenses[j:]):
                if ei + ej + ek == 2020:
                    print(f'\t{ei} + {ej} + {ek} = {ei + ej + ek}')
                    print(f'\t{ei} * {ej} * {ek} = {ei*ej*ek}')
    return

if __name__ == '__main__':
    part1()
    part2()
