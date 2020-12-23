import sys
import re

puzzle_input = [l for l in sys.stdin.read().split('\n')[:-1]]

d = {}
for i, p in enumerate(puzzle_input):
    if p == '':
        puzzle_input = puzzle_input[i + 1:]
        break
    d[p.split(':')[0]] = p.split(': ')[1].strip('"')

# part 1
def parse(d, index):
    prefix = d[index]
    anchor = 0
    while re.search('[0-9]', prefix):
        anchor = re.search('[0-9]+', prefix)
        prefix = prefix[:anchor.start()] + '(' + d[prefix[anchor.start():anchor.end()]] + ')' + prefix[anchor.end():]
    prefix = prefix.replace(' ', '')
    return prefix

def tell_count(d, puzzle_input):
    regex = re.compile(parse(d, '0') + '$')
    count = 0
    for p in puzzle_input:
        if regex.match(p):
            count += 1
    return count

# part 2
d['8'] = '42+'
s = '42 31 | 42 11 31'
results = []
while True:
    t = s.split('|')[-1]
    s = s.replace('11', '42 31')
    t = t.replace('11', '42 11 31')
    s += ' |' + t
    d['11'] = '|'.join(s.split('|')[:-1])
    matches = tell_count(d, puzzle_input)
    if matches not in results:
        results.append(matches)
    else:
        print(matches)
        break