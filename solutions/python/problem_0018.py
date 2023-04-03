from Isolution import ISolution


class Solution(ISolution):
    triangle = [
        [75],
        [95,64],
        [17,47,82],
        [18,35,87,10],
        [20, 4,82,47,65],
        [19, 1,23,75, 3,34],
        [88, 2,77,73, 7,63,67],
        [99,65, 4,28, 6,16,70,92],
        [41,41,26,56,83,40,80,70,33],
        [41,48,72,33,47,32,37,16,94,29],
        [53,71,44,65,25,43,91,52,97,51,14],
        [70,11,33,28,77,73,17,78,39,68,17,57],
        [91,71,52,38,17,14,91,43,58,50,27,29,48],
        [63,66, 4,68,89,53,67,30,73,16,69,87,40,31],
        [4,62,98,27,23, 9,70,98,73,93,38,53,60,4,23],
    ]
    
    @staticmethod
    def incomplete_answer_one():
        s = 0
        last_max_position = 0
        for row in Solution.triangle:
            if last_max_position + 1 < len(row):
                if row[last_max_position] <= row[last_max_position+1]:
                    last_max_position += 1
            print(row[last_max_position])
            s += row[last_max_position]
            
        return str(s)
    
    @staticmethod
    def answer_two() -> str:
        triangle = Solution.triangle
        for k in range(2,len(triangle)+1):
            for i in range(1,len(triangle[-k])+1):
                triangle[-k][i-1] += max(triangle[-k+1][i-1],triangle[-k+1][i])         
        return str(triangle[0][0])

if __name__ == "__main__":
    Solution.debug_mode(__file__)