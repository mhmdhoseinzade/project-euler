from Isolution import ISolution


class Solution(ISolution):

    
    @staticmethod
    def answer_one():
        cache = {}
        def countRoutes(m,n):
            if m == 0 or n == 0:
                return 1
            if cache.get((m,n)):
                return cache[(m,n)]
            
            cache[(m,n)] = countRoutes(m,n-1) + countRoutes(m-1,n)
            return cache[(m,n)]

        
        return str(countRoutes(20,20))    
    
    
if __name__ == "__main__":
    Solution.debug_mode(__file__)