def f(n):
    if n <= 1:
        return n
    return f(n - 1) + f(n - 2)


def f2(n):
    if n <= 1:
        return n
    a = [0] * (n+1)
    a[1] = 1
    for i in range(2, n+1):
        a[i] = a[i-1] + a[i-2]
    return a[n]


print(f(11))
print(f2(11))
