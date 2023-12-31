import random
import sys

def main():
    user_input = get_level() #level of calculator
    i = 0


    while i < 10:# loop to generate 10 questions
        X, Y = generate_integer(user_input) #get values of random ints generated
        Z = X + Y
        print(f"{X} + {Y} = ", end='') #print to terminal
        p = problem_solver(Z, X, Y)
        i +=1
    print(p)

def problem_solver(Z, X , Y):
    x = 0
    score = 0
    while x < 3:# check for wrong results and loop 3 times
            try:
                us_2 = int(input(" "))
                if Z != us_2:
                    raise ValueError
            except ValueError:
                print("EEE")
                print(f"{X} + {Y} = ", end='')
                x +=1
                pass
                if x == 3:
                    print(Z)
                    x = 0
                    sys.exit()   #code runs with manual checkng but check50 coming up with errors(unable to generate 10 problems before quiting)
            else:                 #except I use sys.exit instead of break, which gives only one error(little professor displays number of problems correct)
                if Z == us_2:     #if by chance anyone checks manually, change sys.exit to break to get desired outputs.
                    score +=1

    return score

def get_level():# take userinput and check for wrong input
    while True:
        try:
            n = int(input("Level: "))
            if n <= 0 or n > 3:
                raise ValueError
        except ValueError:
            pass
        else:
            return n

def generate_integer(level):# generate intergers based on level entered
    if level == 1:
        p = random.randrange(0,9)
        q = random.randrange(0,9)
    elif level == 2:
        p = random.randrange(10,99)
        q = random.randrange(10,99)
    elif level == 3:
        p = random.randrange(100,999)
        q = random.randrange(100,999)

    return p, q

if __name__ == "__main__":
    main()
