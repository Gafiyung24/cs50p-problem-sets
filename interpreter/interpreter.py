#accept user input
E = input("Expression: ").strip().split()
#assigning list from split to variables
X = int(E[0])
Y = int(E[2])
# condtional statement to make calculations
if E[1] == "+":
    Z = X + Y
    Z = float(Z)
    print(f"{Z:.1f}")
elif E[1] == "-":
    Z = X - Y
    Z = float(Z)
    print(f"{Z:.1f}")
elif E[1] == "*":
    Z = X * Y
    Z = float(Z)
    print(f"{Z:.1f}")
elif E[1] == "/":
    Z = X / Y
    Z = float(Z)
    print(f"{Z:.1f}")
else:
    print("This operation is not recognised")
