from Isolution import ISolution


class Solution(ISolution):

    @staticmethod
    def answer_one() -> str:
        import math
        current_triangle = 0
        number = 1
        number_of_dividores = 500
        
        while True:
            current_triangle = (number * (number + 1)) // 2
            divisors = 0

            for i in range(1, int(math.sqrt(current_triangle))+1):
                if current_triangle % i == 0:
                    divisors += 2

            if divisors > number_of_dividores:
                return str(current_triangle)
            number += 1        
    
    @staticmethod
    def answer_two() -> str:
        import itertools
        
        def num_divisors(n):
            import math
            end = int(math.sqrt(n))
            
            result = sum(2 for i in range(1,end+1) if n%i == 0)
            
            if end **2 == n:
                result -= 1
            return result
        
        
        triangle = 0
        for i in itertools.count(1):
            triangle += i
            if num_divisors(triangle) > 500:
                return str(triangle)

    @staticmethod
    def answer_three() -> str:
        dec=[dict(), dict(), {2:1}, {3:1}]
        Nbdivi=[0, 1, 2, 2]
        prime=[2,3]
        n=3
        limit = 500
        while True:
            n += 1
            for p in prime:
                if not n%p:
                    dec.append(dec[n//p].copy())
                    if p in dec[n]:
                        dec[n][p]+=1
                    else:
                        dec[n][p]=1
                    nd=1
                    for p,a in dec[n].items():
                        nd*=(a+1)
                    Nbdivi.append(nd)
                    break
                if p*p>n:
                    dec.append({n:1})
                    Nbdivi.append(2)
                    prime.append(n)
                    break

            if n%2:
                if Nbdivi[(n-1)//2]*Nbdivi[n]>limit: 
                    return str((n-1)//2 * n)
            else:
                if Nbdivi[n//2]*Nbdivi[n-1]>limit:
                    return str((n//2)*(n-1))
    
if __name__ == "__main__":
    Solution.debug_mode(__file__)