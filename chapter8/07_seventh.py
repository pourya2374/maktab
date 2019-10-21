data1 = []
data2 = []

for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    data1.append(a + b)
    data2.append(a - b)

a = max(data1) - min(data1)
b = max(data2) - min(data2)
print(max(a, b))
