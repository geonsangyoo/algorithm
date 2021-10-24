import sys
import math

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#23260/input.txt')
else:
  f = sys.stdin

REMAINDER = (10**9) + 7

# N = 1000008
# is_prime = [1]*N
# # We know 0 and 1 are composites
# is_prime[0] = 0
# is_prime[1] = 0

# def sieve():
#   """
#   We cross out all composites from 2 to sqrt(N)
#   """
#   i = 2
#   # This will loop from 2 to int(sqrt(x))
#   while i*i <= N:
#     # If we already crossed out this number, then continue
#     if is_prime[i] == 0:
#       i += 1
#       continue

#     j = 2*i
#     while j < N:
#       # Cross out this as it is composite
#       is_prime[j] = 0
#       # j is incremented by i, because we want to cover all multiples of i
#       j += i

#     i += 1

# sieve()

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6. 
  f = 5
  while f <= r:
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True    


def is_prime_number(i):
  ans = True
  if i > 1:
    num = 2
    while (num * num <= i):
      if i % num == 0:
        ans = False
        break
      num += 1
  return ans

def get_factorial(n):
  ans = 1
  for _ in range(1, n + 1):
    ans = _ * ans
  return ans

def get_combination(n, r):
  num = 1
  denom = math.factorial(r)
  for _ in range(n, n - r, -1):
    num = num * _
  return (num / denom) % REMAINDER

N, K = map(int, f.readline().strip().split())
R = 0
arr = list(map(int, f.readline().strip().split()))
for i in range(N):
  if is_prime(arr[i]):
    R += 1

# print(get_combination(R, K))
print(math.comb(R, K) % REMAINDER)


# n,k = list(map(int, f.readline().split()))
# n = 0
# for _ in f.readline().split():
#   if is_prime[int(_)]==1: n += 1

# print(get_combination(n, k))
# print(math.comb(n, k) % REMAINDER)
