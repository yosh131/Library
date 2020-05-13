def Eratosthenes(n):
    sieve = [True] * (n+1)
    sieve[0] = False
    sieve[1] = False

    primes = []

    for i in range(2,n+1):
        if not sieve[i]:
            continue

        primes.append(i)
        cur = i*2
        while cur<=n:
            sieve[cur] = False
            cur += i
    return primes

def PrimeFactorization2(n,lcm):
    idx = 0
    cur = n
    while cur>1:
        temp = 0
        while cur%primes[idx]==0:
            temp += 1
            cur //= primes[idx]
        lcm[idx] = max(temp, lcm[idx])
        idx += 1
    return lcm

def PrimeFactorization(n):
    ret = [0] * len(primes)
    idx = 0
    cur = n
    while cur>1:
        while cur%primes[idx]==0:
            ret[idx] += 1
            cur //= primes[idx]
        idx += 1
    return ret

N = int(input())
A = list(map(int,input().split()))

primes = Eratosthenes(max(A))
lcm = [0]*len(primes)
for a in A:
    lcm = PrimeFactorization2(a, lcm)

ans = 0
MOD = 10**9+7

for a in A:
    ret = PrimeFactorization(a)
    











