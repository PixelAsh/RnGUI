'''
Author: Ash Sizemore
Assignment: Final Project
Program Name: RnGUI
Program Description: This program will roll D&D Dice automatically.
'''

#import random
import random

#Sets of dice
DiceSix = random.randint(1, 6)
DiceFour = random.randint(1, 4)
DiceEight = random.randint(1, 8)
DiceTen = random.randint(1, 10)
DiceTwenty = random.randint(1, 20)
DiceTwelve = random.randint(1, 12)
DicePercent = random.randint(1, 100)

#Window
from breezypythongui import EasyFrame

class DiceSelect(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "RnGui", width = 300, height = 150)
        self.addButton(text = "Roll a D6", command = self.diceSix, row = 2, column = 0)
    
    def diceSix(self):
        self.addLabel(text = "You rolled " + str(random.randint(1,6)), row = 1, column = 1)

DiceSelect().mainloop()
