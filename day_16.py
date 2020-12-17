import sys
import re
from operator import itemgetter

puzzle_input = [l for l in sys.stdin.read().splitlines()]

start_regex = r"\d+(?=-)"
end_regex = r"(?<=-)\d+"
final_regex = re.compile(start_regex + "|" + end_regex)

ranges = list(map(int, re.findall(final_regex, "".join(puzzle_input))))
ranges = [ranges[i:i + 2] for i in range(0, len(ranges), 2)]

nearby_tickets = list(map(int, re.findall(r"\d+", " ".join(puzzle_input[puzzle_input.index("nearby tickets:") + 1:]))))
my_ticket = list(eval(puzzle_input[puzzle_input.index("your ticket:") + 1]))

ticket_fields = {}
for p in puzzle_input:
    if p == '':
        break
    else:
        f_range = list(map(int, re.findall(final_regex, "".join(p))))
        field = re.findall(r".+(?=:)", p)[0]
        ticket_fields[field] = []
        [[ticket_fields[field].append(j) for j in range(f_range[i], f_range[i + 1] + 1)] for i in range(0, len(f_range), 2)]

# part 1
# sm = 0
# for n in nearby_tickets:
#     flag = 0
#     for r in ranges:
#         if r[0] <= n <= r[1]:
#             flag = 1
#             break
#     if flag == 0:
#         sm += n
# print(sm)

# part 2
nearby_tickets = []
for p in puzzle_input[puzzle_input.index("nearby tickets:") + 1:]:
    nearby_tickets.append(list(eval(p)))

valid_nearby_tickets = []
for n in nearby_tickets:
    append = True
    for num in n:
        invalid = False
        for r in ranges:
            if r[0] <= num <= r[1]:
                invalid = False
                break
            else:
                invalid = True
        if invalid:
            append = False
            break
    if append:
        valid_nearby_tickets.append(n)

field_search = {}
for i in range(len(valid_nearby_tickets[0])):
    l = list(map(itemgetter(i), valid_nearby_tickets))
    field_search[i + 1] = []
    for k, v in ticket_fields.items():
        if set(l).issubset(set(v)):
            field_search[i + 1].append(k)

i = 0
already_removed = []
while i < len(ticket_fields.keys()):
    i += 1
    to_be_elim = ''
    for f in field_search.values():
        if len(f) == 1 and f[0] not in already_removed:
            to_be_elim = f[0]
            already_removed.append(to_be_elim)
            break

    for f in field_search.values():
        if to_be_elim in f and len(f) > 1:
            f.remove(to_be_elim)

mul = 1
for k, v in field_search.items():
    if 'departure' in v[0]:
        mul *= my_ticket[k - 1]
print(mul)