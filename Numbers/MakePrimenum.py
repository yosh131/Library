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


N = 10**6
primes = Eratosthenes(N)
print(len(primes))



