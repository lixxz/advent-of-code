import sys, re

p_in = [l.rstrip('\n') for l in sys.stdin.read().split('\n')]

counts = []
group_answers = ''
# part 1
# for i in p_in:
#     if i != '':
#         group_answers += i
#     elif i == '':
#         counts.append(len(set(group_answers)))
#         group_answers = ''

# part 2
form_in = []
temp = []
for i in p_in:
    if i != '':
        temp.append(i)
    else:
        form_in.append(temp)
        temp = []

for i in form_in:
    count = 0
    for c in set(i[0]):
        if len(re.findall(c, ' '.join(i))) == len(i):
            count += 1
    counts.append(count)

print(sum(counts))