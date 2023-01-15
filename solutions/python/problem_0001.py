from Isolution import ISolution


class Solution(ISolution):

    @staticmethod
    def answer_one() -> str:
        s = 0
        for i in range(1000):
            if i % 3 == 0 or i % 5 == 0:
                s += i
        return str(s)
    
    @staticmethod
    def answer_two() -> str:

        # return str(sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0]))
        return str(sum((i for i in range(1000) if i % 3 == 0 or i % 5 == 0)))

    

    @staticmethod
    def test_answer_three() -> str:
        """
            sum_div(3) + sum_div(5) - sum_div(15)

            3+6+9, ...+ 999 = 3(1+ 2 + 3 + ... + 333) n * (n+1) / 2
            5 + 10 + 15 ... + 995 = 5 (1 + 2 + 3 ... + 199) 999 // 5
        """
        
        def sum_div(n: int) -> int:
            p = 999 // n
            return int(n * (p * (p+1)/2))
        
        return str(sum_div(3) + sum_div(5) - sum_div(15))
    
    

    
    
if __name__ == "__main__":
    Solution.debug_mode(__file__)