import sys
import math

sys.setrecursionlimit(10000)

DEBUG = True
# DEBUG = False

if DEBUG:
  f = open('#23260/input.txt')
else:
  f = sys.stdin

p = (10**9) + 7

'''defining the modulo function.'''
def Mod(n, r, p): 
    arr = [0] * (n + 1);   
           #The array arr is going to store the
           # last row of the triangle 
           # at the end. And last entry  
           # of last row is nCr 
    arr[0] = 1;    
    for i in range(1, (n + 1)):       
        j = min(i, r);  
        while(j > 0): 
            arr[j] = (arr[j] + arr[j - 1]) % p; 
            j -= 1; 
    return arr[r]; 
###################################################
'''
calculate the last digit of n and r for base p, 
then recur 
the remaining digits 
'''
def Lucas(n, r, p): 
    if (r == 0):
        return 1;  
    nth = int(n % p); 
    rth = int(r % p);            
    return (Lucas(int(n / p), int(r / p), p) * Mod(nth, rth, p)) % p; 
########################################################################

def is_prime2(n):
  if n < 2: return True
  for i in range(2, n + 1):
    for j in range(2, int(i ** 0.5) + 1):
      if i % j == 0:
        break
    else:
      return True
  return False

def is_prime(num):
  if num < 2: return True
  for i in range(2,num+1):
    for j in range(2,i):
        if(i%j == 0):
            return False
    else:
        return True
  return True

def power(a, b):
    if b == 0:
        return 1
    if b % 2: 
        return (power(a, b//2) ** 2 * a) % p
    else:
        return (power(a, b//2) ** 2) % p

# lucas theorem to calc C(n,r) % m if m is prime
memory = {} #creating a dictionary to store C(n,r,m) where 0<=r<=n<=9 .
# creating dictionary here also demonstrates memoization
def C(n,r,m):
    if r < 0 or r > n : return 0
    if r == 0 or r == n : return 1
    if n > m :
        return C(n%m,r%m,m) * C(n//m,r//m,m) % m
    if (n,r,m) not in memory:
        memory[(n,r,m)] = (C(n-1,r,m) + C(n-1,r-1,m)) % m #calculating C() recursively
    # print(memory)
    return memory[(n,r,m)]

def mod_exp(b,e,mod):
  r = 1
  while e > 0:
      if (e&1) == 1:
          r = (r*b)%mod
      b = (b*b)%mod
      e >>= 1

  return r

def fact_exp(n,p):
  e = 0
  u = p
  t = n
  while u <= t:
      e += t//u
      u *= p

  return e

def get_base_digits(n,b):
  d = []
  while n > 0:
      d.append(n % b)
      n  = n // b

  return d

def fermat_binom_advanced(n,k,p):
  num_degree = fact_exp(n,p) - fact_exp(n-k,p)
  den_degree = fact_exp(k,p)
  if num_degree > den_degree:
      return 0

  if k > n:
      return 0

  num = 1
  for i in range(n,n-k,-1):
      cur = i
      while cur%p == 0:
          cur //= p
      num = (num*cur)%p

  denom = 1
  for i in range(1,k+1):
      cur = i
      while cur%p == 0:
          cur //= p
      denom = (denom*cur)%p

  return (num * mod_exp(denom,p-2,p))%p

def lucas_binom(n,k,p):
  np = get_base_digits(n,p)
  kp = get_base_digits(k,p)

  # (nCk) = (n0 C k0)*(n1 C k1) ... (ni C ki) (mod p)
  binom = 1
  for i in range(len(np)-1,-1,-1):
      ni = np[i]
      ki = 0
      if i < len(kp):
          ki = kp[i]

      binom = (binom * fermat_binom_advanced(ni,ki,p)) % p

  return binom

n, k = map(int, f.readline().strip().split())
arr = list(map(int, f.readline().strip().split()))

R = 0
for i in range(n):
  if is_prime2(arr[i]):
    R += 1
n = R

if (n < k):
  print(0)
else:
  # print(Lucas(n, k, p))
  print(lucas_binom(n,k,p))
  # print(C(n, k, p))
  # fact = [1 for _ in range(n+1)]

  # for i in range(2, n+1):
  #     fact[i] = fact[i-1] * i % p

  # A = fact[n]
  # B = (fact[n-k] * fact[k]) % p

  # print((A % p) * (power(B, (p-2) % p) % p) % p )
