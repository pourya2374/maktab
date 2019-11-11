import random

n = 5
m = 300000

output = open('input.txt', 'w')

total = random.randint(1, m)
output.write('{}\n'.format(total))
for _ in range(total):
    tmp = random.randint(1, 2)
    if tmp % 2:
        tmp1 = random.randint(1, n)
        tmp2 = random.randint(1, n)
        output.write('Merge {} {}\n'.format(tmp1, tmp2))
    else:
        tmp1 = random.randint(1, n)
        output.write('Height {}\n'.format(tmp1))
output.close()
