import importlib, time

import json,time,os

BASE_DIR = "."
ANSWERS_FILE = "../../ANSWERS.json"
CLASS_NAME = "Solution"
METHOD_PREFIX = "answer"

def main() -> None:
    totaltime = 0
    answers = json.load(open(ANSWERS_FILE))
    for _,_,files in os.walk(BASE_DIR):
        for file in files:
            if file.endswith(".py"):
                file_name = file.split(".")[0]
                if not file_name.startswith("problem_"):
                    continue
                print(f"     Problem {file_name}")
                module = importlib.import_module(f"{file_name}")
                klass = getattr(module, CLASS_NAME)
                method_list = [getattr(klass,method) for method in dir(klass) if method.startswith(METHOD_PREFIX) and callable(getattr(klass,method))]
                for method in method_list:
                    print(f">> {method.__name__} ",end="")
                    starttime = time.time()
                    my_answer = method() # must return string
                    
                    answer_query = file_name.replace("problem_","")
                    answer_query = str(int(answer_query))
                    correct_answer = answers[answer_query]

                    assert my_answer == correct_answer, f"Incorrect Answer file : {my_answer} != {correct_answer} ({file_name}.py {method.__name__})"
                    elapsedtime = time.time() - starttime
                    totaltime += elapsedtime

                    print(f"{elapsedtime} ({correct_answer})")
                if not method_list:
                    print() 
		            
    print(f"total time {totaltime}")


main()