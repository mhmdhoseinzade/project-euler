from Isolution import ISolution


class Solution(ISolution):

    @staticmethod
    def answer_one():
        import math
        def cal_d(n):
            s = 1
            for i in range(2,int(math.sqrt(n))+1):
                if n % i == 0:
                    s += i
                    s += n // i
            return s

        res = 0
        for j in range(10000):
            x = cal_d(j)
            if cal_d(x) == j:
                if x != j:
                    res += j
        return str(res)
    
    @staticmethod
    def answer_two():
        def sumDivisors(x):
            return 1 + sum([ i + x / i for i in range(2, int(x ** 0.5) + 1) if (x % i == 0)]) 
        return str(sum([i for i in range(1,10000) for j in [sumDivisors(i)] if j != i and i == sumDivisors(j)]))
    
    @staticmethod
    def answer_three():

        def AmicableNumbers(num):
            sieve=[1]*(num+1)
            amicable_sum = 0
            for i in range(2,int(num**0.5)+1):
                sieve[i*i] += i
                for k in range(i*(i+1),num+1,i):
                    sieve[k]+= i+k // i
            for i in range(num):
                if sieve[i]<i and sieve[sieve[i]]== i:
                    amicable_sum += i+sieve[i]
            return amicable_sum
        
        return str(AmicableNumbers(10000))


if __name__ == "__main__":
    Solution.debug_mode(__file__)