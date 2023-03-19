from Isolution import ISolution


class Solution(ISolution):  

    @staticmethod
    def isPalindrome(n):
            m = n
            revered_number = 0
            while n>0:
                revered_number = (revered_number * 10) + (n%10)
                n //= 10
            return m == revered_number
    
    @staticmethod
    def answer_one():
        maxp = 0
        for i in range(100,1000):
            for j in range(i,1000):
                p = i * j
                if str(p) == str(p)[::-1] and p > maxp:
                    maxp = p
        return str(maxp)

    @staticmethod
    def answer_two():
        
        largestPalindrome = 0
        for a in range(999,101,-1):
            for b in range(999,a,-1):
                product_ab = a*b

                if product_ab < largestPalindrome:
                    break

                if Solution.isPalindrome(product_ab):
                    largestPalindrome = product_ab
        return str(largestPalindrome)

    @staticmethod
    def answer_three():
            
        largestPalindrome = 0
        for a in range(999,101,-1):
            db = 1 if a%11 == 0 else 11
            for b in range(999,a,-db):
                product_ab = a*b

                if product_ab < largestPalindrome:
                    break

                if Solution.isPalindrome(product_ab):
                    largestPalindrome = product_ab
        return str(largestPalindrome)
    
    @staticmethod
    def answer_four():
        return str(max([x*y for x in range(999,101,-1) for y in range(999,x,-1) if str(x*y) == str(x*y)[::-1]]))

if __name__ == "__main__":
    Solution.debug_mode(__file__)
