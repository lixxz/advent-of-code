import sys
import re

i = [l for l in sys.stdin.read().split('\n')[:-1]]

# part 1
parents = ['shiny gold']

for s in parents:
    for bag in i:
        if s in bag.split('contain')[1]:
            w = bag.split(' ')[0] + ' ' + bag.split(' ')[1]
            if w not in parents:
                parents.append(w)

print(len(parents) - 1) # -1 for shiny gold

# part 2

def child(b):
    total = 0
    ch = []
    for bag in i:
        if b.split(' ')[0] + ' ' + b.split(' ')[1] in bag.split('contain')[0]:
            s_temp = bag.replace(',', '')
            s_temp = s_temp.replace('.', ' ')
            regex = r"\d [a-z]+ [a-z]+"
            ch = re.findall(regex, s_temp.split('contain ')[1])
            break
    for c in ch:
        total += int(c.split(' ')[0])
        total += (int(c.split(' ')[0]) * child((c.split(' ')[1] + ' ' + c.split(' ')[2])))
    return total


print(child('shiny gold'))