"""input("What is your name? :")
print("hello, World")
print("meow\n" * 3, end= "")
def main():
    print_column(3)



def print_column(height):
    for _ in range(height):
        print("#" * 3)


main()
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)

main()"""
user_input = input("name: ")
for i, u in enumerate(user_input):
        if u.isupper():
            user_input = user_input[:i] + "_" + user_input[i:]
            print(user_input)
        else:
            output = user_input
            print(output)
