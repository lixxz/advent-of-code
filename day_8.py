import sys

i = [l.rstrip('\n') for l in sys.stdin.read().split('\n')[:-1]]

# counter = 0
# instruction_executed = []
# index = 0

# while True:
#     if index not in instruction_executed:
#         if i[index].split(' ')[0] == 'acc':
#             instruction_executed.append(index)
#             counter += int(i[index].split(' ')[1])
#             index += 1

#         elif i[index].split(' ')[0] == 'jmp':
#             instruction_executed.append(index)
#             index += int(i[index].split(' ')[1])

#         elif i[index].split(' ')[0] == 'nop':
#             index += 1

#     else:
#         break

jmp_index = []
nop_index = []

for num, j in enumerate(i):
    if j.split(' ')[0] == 'jmp':
        jmp_index.append(num)

    if j.split(' ')[0] == 'nop':
        nop_index.append(num)

for j in jmp_index:
    intructions_ex = []
    counter = 0
    index = 0
    i_copy = i[:]
    i_copy[j] = 'nop ' + i_copy[j].split(' ')[1]
    while index < len(i_copy):
        if index not in intructions_ex:
            if i_copy[index].split(' ')[0] == 'acc':
                intructions_ex.append(index)
                counter += int(i_copy[index].split(' ')[1])
                index += 1

            elif i_copy[index].split(' ')[0] == 'jmp':
                intructions_ex.append(index)
                index += int(i_copy[index].split(' ')[1])

            elif i_copy[index].split(' ')[0] == 'nop':
                index += 1

        else:
            break

    if index == len(i_copy):
        print(counter)
        break

for j in nop_index:
    intructions_ex = []
    counter = 0
    index = 0
    i_copy = i[:]
    i_copy[j] = 'jmp ' + i_copy[j].split(' ')[1]
    while index < len(i_copy):
        if index not in intructions_ex:
            if i_copy[index].split(' ')[0] == 'acc':
                intructions_ex.append(index)
                counter += int(i_copy[index].split(' ')[1])
                index += 1

            elif i_copy[index].split(' ')[0] == 'jmp':
                intructions_ex.append(index)
                index += int(i_copy[index].split(' ')[1])

            elif i_copy[index].split(' ')[0] == 'nop':
                index += 1

        else:
            break

    if index == len(i_copy):
        print(counter)
        break