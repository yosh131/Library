
class PrimeNum:
    def __init__(self, N):
        self.N = N
        [self.is_prime, self.primes, self.min_factor] = self.Eratosthenes(N)

        # i -> primes[j] を対応させる辞書
        # 2 -> 0,  3 -> 1, 5 -> 2, ... 
        self.num_to_prime = dict()
        for i, p in enumerate(self.primes):
            self.num_to_prime[p] = i
        
    def Eratosthenes(self, n):
        # 素数テーブル
        is_prime = [True] * (n+1)
        is_prime[0] = False
        is_prime[1] = False

        # nを割り切る最小の素数を記録
        min_factor = [0] * (n+1)
        min_factor[1] = 1
        
        primes = []

        for i in range(2,n+1):
            if not is_prime[i]:
                continue

            primes.append(i)
            min_factor[i] = i
            for cur in range(i*2, n+1, i):
                is_prime[cur] = False
                if min_factor[cur] == 0:
                    min_factor[cur] = i
                cur += i

        return [is_prime, primes, min_factor]
    
    def PrimeFactorization(self, K):
        # Kの素因数分解を返す
        number = []
        exponent = []
        while K>1:
            ex = 0
            p = self.min_factor[K]
            while K%p==0:
                K //= p
                ex += 1
            number.append(p)
            exponent.append(ex)
        return [number, exponent]

    def LCM(self, A, MOD):
        # A =　[a_0, ..., a_n-1]のLCMを素因数分解の形式で計算してMODで返す
        lcm_e = [0] * len(self.primes)
        for a in A:
            [nums, exs] = self.PrimeFactorization(a)
            for n,e in zip(nums, exs):
                p = self.num_to_prime[n]
                lcm_e[p] = max(lcm_e[p], e)
        
        lcm = 1
        for i, e in enumerate(lcm_e):
            if e!=0:
                lcm *= pow(i,e,MOD)
                lcm %= MOD
        return lcm




N = int(input())
A = list(map(int,input().split()))
MOD = 10**9+7
# 素因数分解の形でLCMを求める

Prime = PrimeNum(max(A))
lcm_e = [0]*(max(A)+1)
for i in range(N):
    nums,exs = Prime.PrimeFactorization(A[i])
    for n,e in zip(nums,exs):
        lcm_e[n] = max(lcm_e[n], e)

LCM = 1
for i in range(len(lcm_e)):
    if lcm_e[i] != 0:   
        LCM *= pow(i, lcm_e[i], MOD)
        LCM %= MOD
ans = 0
for a in A:
    ans += LCM * pow(a, MOD-2, MOD)
    ans %= MOD
print(ans)
    