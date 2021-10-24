n, k, m = map(int, input().split())

def pow(n, k, m):
    if k == 1:
        return n
    pow_half = pow(n, k//2, m)
    if k % 2 == 0:
        return (pow_half ** 2) % m
    else:
        return (pow_half ** 2 * n) % m

factorial = [1] * (m+1)
for idx in range(2, m+1):
    factorial[idx] = (factorial[idx-1] * idx) % m

def inverse(n):
    return pow(factorial[n], m-2, m)

mult = 1
while n != 0 or k != 0:
    n_digit = n % m
    n //= m
    k_digit = k % m
    k //= m

    if n_digit < k_digit:
        mult = 0
        break
    else:
        mult *= factorial[n_digit] * inverse(n_digit - k_digit) * inverse(k_digit)
        mult %= m

print(mult)