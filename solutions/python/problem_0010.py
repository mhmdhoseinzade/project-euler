
from Isolution import ISolution

class Solution(ISolution):

    @staticmethod
    def answer_one():
        import math

        def is_primary(number):
            for i in range(3,int(math.sqrt(number))+1,2):
                if number % i == 0:
                    return False
            return True

        s = 2
        for i in range(3,2000001,2):
            if is_primary(i):
                s += i
        return str(s)

    @staticmethod
    def answer_two() -> str:
        import math
        n = 2000001
        result= [True] * (n + 1)
        result[0] = result[1] = False
        for i in range(int(math.sqrt(n)) + 1):
            if result[i]:
                for j in range(i * i, len(result), i):
                    result[j] = False

        return str(sum([i for (i, isprime) in enumerate(result) if isprime]))

    @staticmethod
    def answer_three() -> str:
        n = 2_000_000
        r = int(n**0.5)
        assert r*r <= n and (r+1)**2 > n
        V = [n//i for i in range(1,r+1)]
        V += list(range(V[-1]-1,0,-1))
        S = {i:i*(i+1)//2-1 for i in V}
        for p in range(2,r+1):
            if S[p] > S[p-1]:  # p is prime
                sp = S[p-1]  # sum of primes smaller than p
                p2 = p*p
                for v in V:
                    if v < p2: break
                    S[v] -= p*(S[v//p] - sp)
        return str(S[n])
    
    @staticmethod
    def answer_four() -> str:
        from itertools import compress
        n = 2_000_000
        def primes(lim):
            "generateur de premier impair"
            assert lim>2
            BA = bytearray
            n = (lim-1)//2
            prime = BA([1])*(n+1)
            prime[0] = 0 # 2*0+1 = 1 n'est pas premier
            # Crible
            for i in range((int(lim**0.5)+1)//2):
                if prime[i]:
                    p = 2*i+1 # p est premier
                    i2 = i*(i+1)<<1
                    prime[i2::p]=BA(1+ (n-i2)//p )
            return compress(range(1,lim+1,2),prime)

        return str(sum(list(primes(n)))+2)

if __name__ == "__main__":
    Solution.debug_mode(__file__)
        