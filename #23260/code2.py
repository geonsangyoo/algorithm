import sys
import math

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#23260/input.txt')
else:
  f = sys.stdin

REMAINDER = (10**9) + 7

n = 1000000

def prime_finder(n):
    number_range = set(range(n, 1, -1))
    primes_list = []
    while number_range:
        prime = number_range.pop()
        primes_list.append(prime)
        number_range.difference_update(set(range(prime*2, n+1, prime)))
    return primes_list

primes = prime_finder(n)
primes.insert(0, 1)

def is_primes(num):
  for i in range(2,num+1):
    for j in range(2,i):
        if(i%j == 0):
            return False
    else:
        return True
  return True


def mod(num, a):
  res = 0

  n = len(num)
  nums = list(map(int, num))
  for i in range(n):
      res = ((res * 10) + nums[i]) % a

  return res

def mod2(a, m):
  return (a % m + m) % m

def intersection(lst1, lst2):
  return set(lst1).intersection(lst2)

N, K = map(int, f.readline().strip().split())
R = 0

arr = list(map(int, f.readline().strip().split()))
# arr_filtered = list(set(arr) & set(primes))
arr_filtered = list(intersection(primes, arr))
ans = math.comb(len(arr_filtered), K)
print(mod(list(str(ans)), REMAINDER))
