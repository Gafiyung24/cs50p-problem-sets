from pyfiglet import Figlet
import sys
import random

user_input = input("Input: ")
figlet = Figlet()
if len(sys.argv) == 1:
    f = figlet.getFonts()
    rf = random.choice(f)
    figlet.setFont(font=rf)
    print(figlet.renderText(user_input))

elif "-f
