from Isolution import ISolution

class Solution(ISolution):

    numbers = """73167176531330624919225119674426574742355349194934
            96983520312774506326239578318016984801869478851843
            85861560789112949495459501737958331952853208805511
            12540698747158523863050715693290963295227443043557
            66896648950445244523161731856403098711121722383113
            62229893423380308135336276614282806444486645238749
            30358907296290491560440772390713810515859307960866
            70172427121883998797908792274921901699720888093776
            65727333001053367881220235421809751254540594752243
            52584907711670556013604839586446706324415722155397
            53697817977846174064955149290862569321978468622482
            83972241375657056057490261407972968652414535100474
            82166370484403199890008895243450658541227588666881
            16427171479924442928230863465674813919123162824586
            17866458359124566529476545682848912883142607690042
            24219022671055626321111109370544217506941658960408
            07198403850962455444362981230987879927244284909188
            84580156166097919133875499200524063689912560717606
            05886116467109405077541002256983155200055935729725
            71636269561882670428252483600823257530420752963450""".replace("\n","").replace(" ","")
    digits = [int(character) for character in numbers]

    @staticmethod
    def answer_one():
        import functools,operator
        mylst = [1] * 13
        my_max = 1
        for digit in Solution.digits:
            mylst.pop(0)
            mylst.append(digit)
            my_max = max(my_max,functools.reduce(operator.mul,mylst))
        return str(my_max)
    
    @staticmethod
    def answer_two() -> str:
        from operator import mul
        from functools import reduce
        return str(max([reduce(mul, Solution.digits[i:i+13]) for i in range(len(Solution.digits)-13)]))
        # return str(max([reduce(lambda x, y: int(x) * int(y), Solution.digits[i:i+13]) for i in range(len(Solution.digits)- 13)]))
    
    @staticmethod
    def answer_three() -> str:
        def max_prod(num_list, length):
            start = 0
            prod_list = []
            while start + length <= len(num_list):
                prod = 1
                for i in num_list[start: start+length]:
                    prod = prod * i
                prod_list.append(prod)
                start += 1
            return max(prod_list)
        
        num_str_list = Solution.numbers.split('0')
        num_list = [[int(i) for i in num] for num in num_str_list if len(num) >= 13]
        prods = [max_prod(num, 13) for num in num_list]
        return str(max(prods))

if __name__ == "__main__":
    Solution.debug_mode(__file__)