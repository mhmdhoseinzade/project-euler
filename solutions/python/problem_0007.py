from Isolution import ISolution

class Solution(ISolution):

    @staticmethod
    def test_answer_one():
        
        def is_primary(number):
            import math
            if number <= 1:
                return False
            for i in range(2,int(math.sqrt(number))+1):
                if number % i == 0:
                    return False
            return True

        wanted_index = 10001
        index = 2
        number = 3
        while index < wanted_index:
            number += 2
            if is_primary(number):
                index += 1

        return str(number)


    
if __name__ == "__main__":
    Solution.debug_mode(__file__)