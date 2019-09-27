import math

# https://www.geeksforgeeks.org/modular-division/


def mod_inverse(b, m):
    g = math.gcd(b, m)
    if g != 1:
        return -1
    else:
        return pow(b, m - 2, m)


def mod_divide(a, b, m):
    a %= m
    inv = mod_inverse(b, m)
    if inv == -1:
        raise Exception
    else:
        return (inv * a) % m


def binomial_coef_seq2(n):
    m = 10**9+7
    k = int(n/2)
    b = [1] * (n + 1)
    for i in range(1, k+1):
        b[i] = mod_divide(b[i-1], i, m) * ((n - i + 1) % m)

    b[k+1:] = b[-k-2::-1]
    return b


n = int(input()) - 1
a = list(map(int, input().split(' ')))
m = 10**9+7

res = [0] * (n + 1)
coef = binomial_coef_seq2(n)

sign = 1
for i in range(n, -1, -1):
    res[i] = (sign * coef[i] * (a[i] % m)) % m
    sign *= -1

print(int(sum(res) % (10**9 + 7)))
