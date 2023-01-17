from Isolution import ISolution


class Solution(ISolution):

    @staticmethod
    def answer_one():
        f1,f2 = 1,2
        sum = 0
        while f1 < 4000000:
            if f1 % 2 == 0:
                sum += f1
            f2,f1 = f1+f2,f2
        return str(sum)

    @staticmethod
    def answer_two():
        x = y = 1
        sum = 0
        while (sum < 4000000):
            sum += (x + y)
            x, y = x + 2 * y, 2 * x + 3 * y
        return str(sum)
    
    @staticmethod
    def answer_three():
        sum = 0
        a = 1
        b = 1
        c = a + b
        while c < 4000000:
            sum += c
            a = b + c
            b = c + a
            c = a + b
        return str(sum)
        
    
if __name__ == "__main__":
    Solution.debug_mode(__file__)
