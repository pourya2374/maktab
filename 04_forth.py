def binomial_coef_seq2(n):
    k = int(n/2)
    b = [1] * (n + 1)
    for i in range(1, k+1):
        b[i] = b[i-1] * (n - i + 1) / i

    b[k+1:] = b[-k-2::-1]
    return b


n = int(input()) - 1
a = list(map(int, input().split(' ')))

res = [0] * (n + 1)
coef = binomial_coef_seq2(n)
sign = 1
for i in range(n, -1, -1):
    res[i] = sign * coef[i] * a[i]
    sign *= -1

print(int(sum(res) % (10**9 + 7)))
