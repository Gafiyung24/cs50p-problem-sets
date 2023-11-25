import random


def main():
    user_input = get_level()
    generate_integer(user_input)



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