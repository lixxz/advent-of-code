import sys

puzzle_input = [l for l in sys.stdin.read().split('\n')[:-1]]

m = ''
memory = {}
# part 1
# for p in puzzle_input:
#     if p[:4] == 'mask':
#         m = p.split(' = ')[1]
#         continue
#     num = list(bin(int(p.split(' = ')[1]))[2:].zfill(len(m)))

#     for i in range(len(m)):
#         if m[i] == 'X':
#             continue
#         num[i] = m[i]
    
#     memory[int(p.split('[')[1].split(']')[0])] = int(''.join(num), base=2)
    
# print(sum(memory.values()))

# part 2
for p in puzzle_input:
    if p[:4] == 'mask':
        m = p.split(' = ')[1]
        continue
    num = list(bin(int(p.split('[')[1].split(']')[0]))[2:].zfill(len(m)))

    for i in range(len(m)):
        if m[i] == '0':
            continue
        num[i] = m[i]

    c = 2 ** num.count('X')
    for i in range(c):
        bin_rep = bin(i)[2:].zfill(num.count('X'))
        temp = num.copy()
        for b in bin_rep:
            temp[''.join(temp).find('X')] = b
        memory[''.join(temp)] = int(p.split(' = ')[1])
print(sum(memory.values()))