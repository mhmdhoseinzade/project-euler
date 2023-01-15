# from urllib.request import urlopen
import requests,htmlmin
PROBLEM_BASE_URL = "https://projecteuler.net/problem={}"

problem_number = 1
session = requests.Session()

while True:
    try:
        with requests.Session() as s:
            response = s.get(PROBLEM_BASE_URL.format(problem_number))
            if response.status_code != 200:
                break
            body = response.text
            body_to_str = body
        # with urlopen(PROBLEM_BASE_URL.format(problem_number)) as response:
        #     if response.getcode() != 200:
        #         break
        #     body = response.read()
        #     body_to_str = body.decode("utf-8")
            if not body_to_str:
                break
            body_to_str = body_to_str.replace(
                "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js",
                "js/tex-mml-chtml.js"
            )
            body_to_str = body_to_str.replace(
                "https://polyfill.io/v3/polyfill.min.js?features=es6",
                "js/polyfill.min.js"
            )
            
            #minify html
            body_to_str = htmlmin.minify(body_to_str)
            
            with open("problem_{:04d}.html".format(problem_number),"w",encoding="utf-8") as problem_file:
                problem_file.write(body_to_str)
        print("problem {} saved.".format(problem_number))
        problem_number += 1
    except Exception as e:
        print(str(e))
        print("error while saving problem {}".format(problem_number))
        break
    