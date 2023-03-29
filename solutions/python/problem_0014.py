
from Isolution import ISolution


class Solution(ISolution):

    @staticmethod
    def answer_one():
        
        def count_length(n):
            
            if n == 1:
                return 1
            elif n % 2 == 0:
                return 1 + (count_length(n // 2))
            else:
                return 1 + (count_length(3 * n + 1))

        return str(max(range(1,1000000), key=count_length))


    @staticmethod
    def answer_two():

        def distance(n, cache={1:1}):
            if n not in cache:
                if n % 2 == 0:
                    cache[n] = distance(n // 2) + 1
                else:
                    cache[n] = distance(3 * n + 1) + 1
            
            return cache[n]

        return str(max(range(1,1000000), key=distance))


if __name__ == "__main__":
    Solution.debug_mode(__file__)