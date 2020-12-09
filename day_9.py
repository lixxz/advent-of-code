import sys

i = [int(l) for l in sys.stdin.read().split('\n')[:-1]]

window = 2

def if_sum(l, x):
    for p in range(len(l)):
        for q in range(p+1, len(l)):
            if l[p] + l[q] == x:
                return True
    return False

for n, x in enumerate(i[25:]):
    if not if_sum(i[n:n + 25], x):
        print(n, x)
        break

def does_sum(window, l, x):
    for p in range(len(l)):
        sm = l[p]
        if p + window < len(l):
            for k in range(p+1, p+window):
                sm += l[k]
            if sm == x:
                return True, min(l[p:k + 1]) + max(l[p:k + 1])
        else:
            continue
    return False, None

while True:
    r = does_sum(window, i[:n] + i[n+1:], x)
    if r[0] == False:
        window = window + 1
    else:
        print(r[1])
        break