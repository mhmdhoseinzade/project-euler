from Isolution import ISolution


class Solution(ISolution):

    @staticmethod
    def answer_one():
        import math
        def is_abundant(n):
            s = 1
            m = math.sqrt(n)
            if  m == int(m):
                s-= m
            for i in range(int(m),1,-1):
                if n % i == 0:
                    s += (i + n // i)
                if s > n:
                    return True
            return s > n
        
        abundant_numbers = set(i for i in range(1,28124) if is_abundant(i))
        
        def has_abundant_sum(i):
            return any(i-a in abundant_numbers for a in abundant_numbers)

        return str(sum(i for i in range(1,28124) if not has_abundant_sum(i)))
    
    @staticmethod
    def answer_two():
        def is_abundant(n):
            m, s = n ** 0.5, 1
            if m == int(m): 
                s -= int(m)
            m = int(m//1) + 1
            for i in range(2, m):
                if n%i == 0:
                    s += i + (n/i)
            return s > n
        
        a, s = set(), 0
        for i in range(1, 28124):
            if is_abundant(i):
                a.add(i)
            if not any((i - j) in a for j in a):
                s += i
        return str(s)


if __name__ == "__main__":
    Solution.debug_mode(__file__)