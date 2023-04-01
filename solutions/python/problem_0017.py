from Isolution import ISolution


class Solution(ISolution):
    
    @staticmethod
    def answer_one():
        guide_map = {
            1: {
                1: 3,
                2: 3,
                3: 5,
                4: 4,
                5: 4,
                6: 3,
                7: 5,
                8: 5,
                9: 4,
                10: 3,
                11: 6,
                12: 6,
                13: 8,
                14: 8,
                15: 7,
                16: 7,
                17: 9, 
                18: 8,
                19: 8, 

            },

            2:{
                2: 6,
                3: 6,
                4: 5,
                5: 5,
                6: 5,
                7: 7,
                8: 6,
                9: 6,
            },
        }
        s = 11 # including 1000 at the begining
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    number_letters_count = 0

                    res = guide_map[1].get(j*10 + k)
                    if not res:
                        res2 = guide_map[1].get(k)
                        if res2:
                            number_letters_count += res2
                        res = guide_map[2].get(j)   

                    if res:
                        number_letters_count += res

                    res = guide_map[1].get(i)
                    
                    if res:
                        number_letters_count += (res + 7)
                        if k != 0 or j != 0:
                            number_letters_count += 3
                    s += number_letters_count
        return str(s)      
                    
    def answer_two() -> str:
        s={
            0:"",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",
            7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",
            13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",
            17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",
            30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",
            80:"eighty",90:"ninety"
        }

        for i in range(1,1000):
            if(not i in s.keys()):
                if(i<100):
                    s[i]=s[i//10 * 10] + s[i%10]
                else:
                    s[i]=s[i//100]+"hundred"
                    if(i%100):
                        s[i] += "and"+s[i%100]
        
        s[1000]="onethousand"
        total=0
        for i in s.values():
            total+=len(i)
        return str(total)

if __name__ == "__main__":
    Solution.debug_mode(__file__)