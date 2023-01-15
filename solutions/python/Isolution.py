
class ISolution:
    
    @classmethod
    def debug_mode(cls,file_name):
        import time,json,os
        METHOD_PREFIX = "test"
        ANSWERS_FILE = "../../ANSWERS.json"
        method_list = [getattr(cls,method) for method in dir(cls) if method.startswith(METHOD_PREFIX) and callable(getattr(cls,method))]
        answers = json.load(open(ANSWERS_FILE))
        for method in method_list:
            file_name = os.path.basename(file_name).split(".")[0]
            print(f">> {method.__name__}\n")
            starttime = time.time()
            print("-=-=-=-= OUTPUT =-=-=-=")
            my_answer = method()
            print("-=-=-=-=-=-=-=-=-=-=-=-\n")
            

            answer_query = file_name.replace("problem_","")
            answer_query = str(int(answer_query))

            correct = answers[answer_query]
            check_mark = 'OK' if correct == my_answer else ""
            print(f"correct answer : {correct}")
            print(f"my answer : {my_answer} {check_mark}")
            print(f"Elapsed Time: {time.time() - starttime}\n")
