import random

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12

def generate_problem(level):
    left = random.randint(pow(MIN_OPERAND, level), pow(MAX_OPERAND, level))
    right = random.randint(pow(MIN_OPERAND, level), pow(MAX_OPERAND, level))
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

for i in range(1,4):
    points = 0
    lifes = 3
    if lifes < 0:
        break
        print("You have lost.")
    print("Level 1!\n")
    while points < 3:
        expr, answer = generate_problem(i)
        print("Give and answer!")
        print(expr)
        user_answer = int(input())
        if user_answer == answer:
            points += 1
            print("Congratulations. You points: ", points)
        else:
            lifes -=1
            print("Bad. Your lives:", lifes)

    







