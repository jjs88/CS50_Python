import random

def solve_problem(problems):
    solved:int = 0
    
    #for each problem, have the user try to solve
    for problem in problems:
        tries = 3
        x,y,z = problem.split(" ")

        while True:
            try:
                prompt:int = int(input(f"{str(problem) + " = "}"))

                if int(x) + int(z) == int(prompt):
                    solved +=1
                    break
                elif int(tries) == 1:
                    answer:int = int(x) + int(z)
                    display_answer:str = str(problem) + " = " + str(answer)
                    print(display_answer)
                    break
                else:
                    tries = tries -1
                    print("EEE")
            except ValueError:
                pass
    
    return solved

def create_math_problems(level):
    problems:list = []
    counter = 1

    while counter <= 10:
        x:int = generate_integer(level)
        y:int = generate_integer(level)

        problem:str = str(x) + " + " + str(y)
        problems.append(problem)

        counter+=1

    return problems

def get_level():
    valid_levels:list = [1,2,3]
    while True:
        try:
            level_choice:int = int(input("Level: "))

            if level_choice not in valid_levels:
                pass
            else:
                break
        
        except ValueError:
            pass
    
    return level_choice

def generate_integer(level:int):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)
    
def main():
    level:int = get_level()
    problems:list = create_math_problems(level)
    solved:int = solve_problem(problems)
    print(f"Solved: {solved}")

if __name__ == "__main__":
    main()