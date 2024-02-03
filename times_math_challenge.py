import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12

def generate_problem(level):
    left = random.randint(level*MIN_OPERAND, level*MAX_OPERAND)
    right = random.randint(level*MIN_OPERAND, level*MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

points = 0
problem_num = 1
lifes = 3
bad = 0

levels = input("How many levels do you want to play?")

if levels.isdigit() == False:
    print("Please, give a number!\n")
    levels = input("How many level do you want to play?")


input("Press any KEY to start!")

start_time = time.time()

for i in range(1,int(levels)+1):    
    count = 0
    if lifes <= 0:
        print("You have lost.")
        break
        
    lifes = 3
    
    print(f"Level {i}!\nYou have {lifes} lives!")
    while count < 5:
        expr, answer = generate_problem(i)
        print(f"Problem #{problem_num}. Give an answer!")
        problem_num += 1
        print(expr)
        user_answer = input()
        count += 1
        if user_answer == str(answer):
            points += 1
            print("Congratulations. You points: ", points)
        else:
            lifes -=1
            bad += 1
            print("Bad. Your lives:", lifes)

    
end_time = time.time()
total_time = end_time - start_time

if lifes > 0:
    score = f"It took you {round(total_time, 2)} second to finish the challenge with {levels} levels. Your score is {round(points/(points+bad), 5)*100}%."
    print(score)
    print_score = input("Do you want to safe your score? Press Y for yes.")
    if print_score.lower() == "y":
        name = input("Please share your name: ")
        with open(f'score-{name}.txt', 'w') as f:
            f.write(f'Name: {name} | Levels: {levels} | Time: {round(total_time, 2)} | Score: {round(points/(points+bad), 4)*100}%')
    
else:
    print("You didn't finish the challenge!")



