import sys

i = sorted([int(l) for l in sys.stdin.read().split('\n')[:-1]])

# part 1
one_diff = 1
three_diff = 1

for idx in range(1, len(i)):
    if i[idx] - i[idx - 1] == 3:
        three_diff += 1
    elif i[idx] - i[idx - 1] == 1:
        one_diff += 1

print(three_diff, one_diff, three_diff * one_diff)

# part 2
def no_of_comb(v, l, i):
    total = 0
    if v == i[-1]:
        total += 1
    else:
        for n in range(1, 4):
            if v + n in i:
                if v + n not in l:
                    l[v + n] = no_of_comb(v + n, l, i)
                total += l[v + n]
    return total

print(no_of_comb(0, {}, i))