from Isolution import ISolution

class Solution(ISolution):    

    @staticmethod
    def answer_one():
        s = 0
        t = 0
        for i in range(1,101):
            s += i**2
            t+= i

        res = (t ** 2) - s
        return str(res)
    
    @staticmethod
    def answer_two() -> str:
        n = 100
        sum_sq = n*(n+1)*(2*n+1)//6
        s = (n*(n+1)//2)**2
        return str(s - sum_sq)
    
    @staticmethod
    def answer_there() -> str:
        r = range(1,101)
        return str(sum(r)** 2- sum([x** 2 for x in r]))
    
    @staticmethod
    def answer_four():
        n = 100
        return str(n * (n ** 2 - 1) * (3 * n + 2) // 12)


if __name__ == "__main__":
    Solution.debug_mode(__file__)