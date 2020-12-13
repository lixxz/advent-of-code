import sys

puzzle_input = [l for l in sys.stdin.read().split('\n')[:-1]]

directions = {'N': [], 'W': [], 'E': [], 'S': []}
current_direction = 'E'
rotation_order_left = 'NWSE'
rotation_order_right = 'NESW'

# part 1
# for p in puzzle_input:
#     if p[0] in 'FB':
#         directions[current_direction].append(int(p[1:]))
#     elif p[0] in 'NEWS':
#         directions[p[0]].append(int(p[1:]))
#     elif p[0] == 'R':
#         current_direction = rotation_order_right[(rotation_order_right.index(current_direction) + (int(p[1:]) / 90)) % 4]
#     elif p[0] == 'L':
#         current_direction = rotation_order_left[(rotation_order_left.index(current_direction) + (int(p[1:]) / 90)) % 4]

# print(abs(sum(directions['N']) - sum(directions['S'])) + abs(sum(directions['E']) - sum(directions['W'])))

# part 2
waypoint_start = {'N': [1], 'W': [], 'E': [10], 'S': []}
for p in puzzle_input:
    if p[0] in 'FB':
        directions['N'].append(sum(waypoint_start['N']) * int(p[1:]))
        directions['E'].append(sum(waypoint_start['E']) * int(p[1:]))
        directions['W'].append(sum(waypoint_start['W']) * int(p[1:]))
        directions['S'].append(sum(waypoint_start['S']) * int(p[1:]))
    elif p[0] in 'NEWS':
        waypoint_start[p[0]].append(int(p[1:]))
    elif p[0] == 'R':
        temp = {}
        temp[rotation_order_right[(rotation_order_right.index('N') + (int(p[1:]) / 90)) % 4]] = waypoint_start['N']
        temp[rotation_order_right[(rotation_order_right.index('E') + (int(p[1:]) / 90)) % 4]] = waypoint_start['E']
        temp[rotation_order_right[(rotation_order_right.index('W') + (int(p[1:]) / 90)) % 4]] = waypoint_start['W']
        temp[rotation_order_right[(rotation_order_right.index('S') + (int(p[1:]) / 90)) % 4]] = waypoint_start['S']
        waypoint_start = temp
    elif p[0] == 'L':
        temp = {}
        temp[rotation_order_left[(rotation_order_left.index('N') + (int(p[1:]) / 90)) % 4]] = waypoint_start['N']
        temp[rotation_order_left[(rotation_order_left.index('E') + (int(p[1:]) / 90)) % 4]] = waypoint_start['E']
        temp[rotation_order_left[(rotation_order_left.index('W') + (int(p[1:]) / 90)) % 4]] = waypoint_start['W']
        temp[rotation_order_left[(rotation_order_left.index('S') + (int(p[1:]) / 90)) % 4]] = waypoint_start['S']
        waypoint_start = temp

print(abs(sum(directions['N']) - sum(directions['S'])) + abs(sum(directions['E']) - sum(directions['W'])))