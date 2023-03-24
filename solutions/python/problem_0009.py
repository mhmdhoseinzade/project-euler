from Isolution import ISolution

class Solution(ISolution):

    @staticmethod
    def answer_one():
        sum_of_numbers = 1000
        for a in range(1,sum_of_numbers):
            for b in range(a+1,sum_of_numbers):
                if (a ** 2) + (b ** 2) == ((sum_of_numbers - a - b) ** 2):
                    return str(a * b * (sum_of_numbers - a - b))

    @staticmethod          
    def answer_two() -> str:
        for c in range(334,500):
            for a in range(1, (1000-c)//2):
                b = (1000 - c) - a
                if a**2 + b**2 == c**2:
                    return str(a*b*c)  
    


if __name__ == "__main__":
    Solution.debug_mode(__file__)