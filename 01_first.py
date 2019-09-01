q = int(input().strip())
divisions = list(map(int, input().split(' ')))

suggestions = []
for n in range(1, 1001):
    result = sum([n % division for division in divisions])
    if result == 0:
        suggestions.append(result)
print(len(suggestions))
