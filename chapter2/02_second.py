n = int(input())
inputs = [input().strip().split(' ') for _ in range(n)]
inputs = [(item[1], item[2]) for item in inputs]
inputs = sorted(inputs, key=lambda a: a[0])

count = 0
result = {}
for item in inputs:
    if item[1] == '+':
        count += 1
    elif item[1] == '-':
        count -= 1
    result[item[0]] = count

max_count = 0
max_time = '00:00'
for key, value in result.items():
    if value >= max_count:
        max_count = value
        max_time = key
print(max_time)
