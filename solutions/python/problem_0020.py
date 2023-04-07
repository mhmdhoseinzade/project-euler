from Isolution import ISolution


class Solution(ISolution):

    @staticmethod
    def answer_one():
        from functools import reduce

        return str(reduce(lambda x,y: x +y, [int(i) for i in str(reduce(lambda x,y: x*y, range(1,100)))]))
    
    @staticmethod
    def answer_two():
        def fac(n):
            if n == 0: return 1
            else: return n * fac(n-1)

        return str(sum(int(n) for n in str(fac(100))))
         


if __name__ == "__main__":
    Solution.debug_mode(__file__)