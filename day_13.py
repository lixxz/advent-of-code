import sys

puzzle_input = [l for l in sys.stdin.read().split('\n')[:-1]]
puzzle_input[1] = puzzle_input[1].split(',')
waiting_time = {}

for p in puzzle_input[1]:
    if p != 'x':
        waiting_time[int(p)] = int(p) - int(puzzle_input[0]) % int(p)

k = min(waiting_time, key=waiting_time.get)
print(waiting_time[k] * k)

# part 2
def crt(pairs):
    M = 1
    for x, mx in pairs:
        M *= mx
    total = 0
    for x, mx in pairs:
        b = M // mx
        total += x * b * pow(b, mx-2, mx)
        total %= M
    return total

pairs = []
for i, n in enumerate(puzzle_input[1]):
    if n == 'x':
        continue
    n = int(n)
    pairs.append((n - i, n))
print(crt(pairs))