from Isolution import ISolution


class Solution(ISolution):
    
    @staticmethod
    def answer_one() -> str:
        from functools import reduce
        def least_common_multiple(a,b):
            if a < b:
                a,b = b,a
            mul = a * b
            while b:
                a,b = b, a%b
            return mul // a
        
        result = reduce(least_common_multiple,range(1,21))
        return str(result)

    @staticmethod
    def answer_two() -> str:
        res = 1
        for i in range(1,21):
            if res % i > 0:
                for j in range(1,21):
                    if (res * j) % i == 0:
                        res *= j
                        break
        return str(res)

    @staticmethod
    def test_answer_three() -> str:
        """ Code Source : https://projecteuler.net/action=redirect;post_id=1441 """
        def delbart(t,n):
            if n > 0:
                if not (t%n):
                    if delbart(t, n-1):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return True

        i = 20
        while not delbart(i,20):
            i +=20
        return str(i)

    
if __name__ == "__main__":
    Solution.debug_mode(__file__)