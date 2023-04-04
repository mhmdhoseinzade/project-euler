from Isolution import ISolution


class Solution(ISolution):

    @staticmethod
    def answer_one():
        import datetime

        return str(sum(int(datetime.datetime(y,m,1).weekday() == 6) for y in range(1901, 2001) for m in range(1, 13)))
    
        # count = 0
        # for y in range(1901,2001):
        #     for m in range(1,13):
        #         if datetime.datetime(y,m,1).weekday() == 6:
        #             count += 1
        # return str(count)
        
    
    @staticmethod
    def answer_two():
        number_of_first_day_in_100_year = 12 * 1 * 100
        sunday_interval = 7
        return str(number_of_first_day_in_100_year // sunday_interval)

    @staticmethod
    def answer_three():
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
        day = 2
        count = 0
        for i in range (1901,2001):
            for j in range (0,12):
                if i % 4 != 0:
                    day+=months[j]%7
                else:
                    if j == 1:
                        day += 29 % 7
                    else:
                        day += months[j]%7
                if day % 7 == 0:
                    count += 1
        return str(count)


if __name__ == "__main__":
    Solution.debug_mode(__file__)