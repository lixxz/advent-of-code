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
def parse_iter(d, index):
    prefix = d[index]
    anchor = 0
    while re.search('[0-9]', prefix):
        anchor = re.search('[0-9]+', prefix)
        prefix = prefix[:anchor.start()] + '(' + d[prefix[anchor.start():anchor.end()]] + ')' + prefix[anchor.end():]
    prefix = prefix.replace(' ', '')
    return prefix

regex = re.compile(parse_iter(d, '0') + '$')
count = 0

for p in puzzle_input:
    if regex.match(p):
        count += 1
print(count)