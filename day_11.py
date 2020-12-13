import sys
from copy import deepcopy

puzzle_input = [[list(l) for l in sys.stdin.read().split('\n')[:-1]]]

def any_occupied_adjacent_seats(i, j):
    occupied_count = 0
    for n in range(max(i-1, 0), min(i+2, len(puzzle_input[-1]))):
        for p in range(max(j-1, 0), min(j+2, len(puzzle_input[-1][j]))):
            if n == i and p == j:
                continue
            elif puzzle_input[-1][n][p] == '#':
                occupied_count += 1
    return bool(occupied_count), occupied_count

def num_occupied_seats(state):
    count = 0
    for i in state:
        for j in i:
            if j == '#':
                count += 1
    return count

# while True:
#     c = deepcopy(puzzle_input[-1])
#     for i in range(len(puzzle_input[-1])):
#         for j in range(len(puzzle_input[-1][i])):
#             if puzzle_input[-1][i][j] == '.':
#                 continue
#             occupied, occupied_count = any_occupied_adjacent_seats(i, j)
#             if puzzle_input[-1][i][j] == 'L' and occupied == False:
#                 c[i][j] = '#'
#             elif puzzle_input[-1][i][j] == '#' and occupied_count >= 4:
#                 c[i][j] = 'L'
#     if c == puzzle_input[-1]:
#         print(num_occupied_seats(c))
#         break
#     puzzle_input.append(c)

# part 2
def any_occupied_adjacent_seats_part2(i, j):
    occupied_count = 0
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if x == 0 and y == 0:
                continue
            counter = 1
            while 0 <= i + counter*x < len(puzzle_input[-1]) and 0 <= j + counter*y < len(puzzle_input[-1][i]):
                if puzzle_input[-1][i + counter*x][j + counter*y] == '#':
                    occupied_count += 1
                    break
                elif puzzle_input[-1][i + counter*x][j + counter*y] == 'L':
                    break
                counter += 1
    return bool(occupied_count), occupied_count

while True:
    c = deepcopy(puzzle_input[-1])
    for i in range(len(puzzle_input[-1])):
        for j in range(len(puzzle_input[-1][i])):
            if puzzle_input[-1][i][j] == '.':
                continue
            occupied, occupied_count = any_occupied_adjacent_seats_part2(i, j)
            if puzzle_input[-1][i][j] == 'L' and occupied == False:
                c[i][j] = '#'
            elif puzzle_input[-1][i][j] == '#' and occupied_count >= 5:
                c[i][j] = 'L'
    if c == puzzle_input[-1]:
        print(num_occupied_seats(c))
        break
    puzzle_input.append(c)