# ***** oo*oo *ooo* **o** oo*oo *ooo*
# oo*oo o***o oo*oo *o*o* o***o *o*o*
# oo*oo *ooo* *ooo* *ooo* *ooo* *ooo*

line1 = input()
line2 = input()
input()

l1 = []
for i in range(5, len(line1) + 1, 5):
    l1.append(line1[i-5:i])
l2 = []
for i in range(5, len(line2) + 1, 5):
    l2.append(line2[i-5:i-4])

result = []
for a, b in zip(l1, l2):
    l = a + b
    if l == '*****o':
        result.append('T')
    elif l == 'oo*ooo':
        result.append('A')
    elif l == '*ooo*o':
        result.append('X')
    elif l == '**o***':
        result.append('M')
    elif l == '*ooo**':
        result.append('N')
print(''.join(result))
