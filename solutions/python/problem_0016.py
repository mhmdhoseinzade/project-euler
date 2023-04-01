from Isolution import ISolution


class Solution(ISolution):
    
    @staticmethod
    def answer_one():
        return str(sum(map(int, list(str(2**1000)))))
        
        # return str(sum(int(digit) for digit in str(2**1000)))
        
        # from functools import reduce
        # return str(reduce(lambda x, y: x + y, [int(i) for i in str(2 ** 1000)]))


if __name__ == "__main__":
    Solution.debug_mode(__file__)