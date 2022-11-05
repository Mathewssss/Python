import random
from random import sample
def euro_milhoes():
    play = input("Want to try your luck?\n Press 'Y' for Yes or 'N' for No: ")
    draw_numbers = list(range(1,51))
    stars_numbers = list(range(1, 13))
    draw = random.sample(draw_numbers,5)
    stars = random.sample(stars_numbers, 2)
    if play == "Y" or play == 'y':
        print(f'Your lucky numbers are: {draw} \nAnd the stars are: {stars}')
        return euro_milhoes()
    if play == "N" or play == "n":
        print('See you next time :)')
    else:
        print("Must choose an option :/")
        return euro_milhoes()
    
euro_milhoes()