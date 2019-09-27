import string

n = int(input().strip())
inputs = []
for i in range(1, n+1):
    line = input().strip().split(' ')
    inputs.append(line)

variables = {}
seen_lines = []
current_line = 1
output = []

while current_line < n + 1:
    if current_line in seen_lines:
        print(-1)
        exit()

    line = inputs[current_line - 1]
    if line[0] == 'assign':
        tmp1 = variables.get(line[3], 0) if len(line[3]) == 1 and line[3] not in string.digits else int(line[3])
        tmp2 = variables.get(line[5], 0) if len(line[5]) == 1 and line[5] not in string.digits else int(line[5])
        variables[line[1]] = (tmp1 + tmp2) % (10**9 + 7)
        current_line += 1
    elif line[0] == 'cout':
        output.append(variables.get(line[1], 0) if len(line[1]) == 1 and line[1] not in string.digits else int(line[1]))
        current_line += 1
    elif line[0] == 'goto':
        seen_lines.append(current_line)
        current_line = int(line[1])

print(*output, sep='\n')
