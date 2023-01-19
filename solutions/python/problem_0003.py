from Isolution import ISolution


class Solution(ISolution):

    @staticmethod
    def answer_one():
        import math
        number = 600851475143
        maximum = 0
        for i in range(1,int(math.sqrt(number)),2):
            if number % i == 0:
                prime = True
                for j in range(2,int(math.sqrt(i))):
                    if i % j == 0:
                        prime=False
                if prime:
                    maximum = i
        return str(maximum)

    def answer_two():
        from math import sqrt
        primes = {2}
        value = 3
        number = 600851475143
        while value < sqrt(number):
            isPrime = True
            for k in primes:
                if value % k == 0:
                    isPrime = False
                    value += 2
            if isPrime:
                primes.add(value)
                if number % value == 0:
                    number = number // value
        return str(number)

    def answer_three():
        d, n = 3, 600851475143
        while (d * d < n):
            if n % d == 0:
                 n = n // d
            else:
                 d += 2
        return str(n)

if __name__ == "__main__":
    Solution.debug_mode(__file__)
