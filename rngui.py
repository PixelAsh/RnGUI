'''
Author: Ash Sizemore
Assignment: Final Project
Program Name: RnGui
Program Description: This program will roll D&D Dice automatically.
'''

#import random function for the dice rolls
import random

#Sets of dice(For Reference)
DiceSix = random.randint(1, 6)
DiceFour = random.randint(1, 4)
DiceEight = random.randint(1, 8)
DiceTen = random.randint(1, 10)
DiceTwenty = random.randint(1, 20)
DiceTwelve = random.randint(1, 12)
DicePercent = random.randint(1, 100)

#Create Window
from breezypythongui import EasyFrame
from tkinter import PhotoImage, N, S, W, E

class DiceSelect(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "RnGui", width = 800, height = 800, resizable = False, background = "#e5decf")
        
    #Logo Image and D20 Images
        imageLabel = self.addLabel(text= "", row = 0, column = 2, sticky = N+S+W+E, columnspan = 3, background = "#e5decf")
        self.image = PhotoImage(file = "rnguilogo.png")
        imageLabel["image"] = self.image
        
        d20Label = self.addLabel(text= "", row = 0, column = 1, sticky = N+S+W+E, background = "#e5decf")
        self.d20Img = PhotoImage(file = "d20.png")
        d20Label["image"] = self.d20Img
        
        d20Label2 = self.addLabel(text= "", row = 0, column = 5, sticky = N+S+W+E, background = "#e5decf")
        d20Label2["image"] = self.d20Img

        #Defining the total roll variable
        self.totalRoll = 0
        
        #Adds a popup window that explains how to use the program
        self.messageBox(title = "Tutorial", message = "To use this program select the dice you want to roll and press the roll selected button. You can select multiple dies!")

    #Adding Buttons
        self.diceSixCB = self.addCheckbutton(text = "Roll a D6", row = 2, column = 0)
        self.diceFourCB = self.addCheckbutton(text = "Roll a D4", row = 2, column = 1)
        self.diceEightCB = self.addCheckbutton(text = "Roll a D8", row = 2, column = 2)
        self.diceTenCB = self.addCheckbutton(text = "Roll a D10", row = 2, column = 3)
        self.diceTwelveCB = self.addCheckbutton(text = "Roll a D12", row = 2, column = 4)
        self.dicePercentCB = self.addCheckbutton(text = "Roll a D100", row = 2, column = 5)
        self.diceTwentyCB = self.addCheckbutton(text = "Roll a D20", row = 2, column = 6)

    #Roll Selected Button
        self.addButton(text = "Roll Selected", command = self.rollAll, row = 3, column = 3)

#Calculating Dice rolls depending on which checkbox is checked
    def rollAll(self):
        
        if self.diceSixCB.isChecked():
            self.diceSixRoll = random.randint(1, 6)
        else:
            self.diceSixRoll = 0
            
        if self.diceFourCB.isChecked():
            self.diceFourRoll = random.randint(1, 4)
        else:
            self.diceFourRoll = 0
            
        if self.diceEightCB.isChecked():
            self.diceEightRoll = random.randint(1, 8)
        else:
            self.diceEightRoll = 0
            
        if self.diceTenCB.isChecked():
            self.diceTenRoll = random.randint(1, 10)
        else:
            self.diceTenRoll = 0

        if self.diceTwelveCB.isChecked():
            self.diceTwelveRoll = random.randint(1, 12) 
        else: 
            self.diceTwelveRoll = 0
        
        if self.dicePercentCB.isChecked():
            self.dicePercentRoll = random.randint(1, 100) 
        else: 
            self.dicePercentRoll = 0
            
        if self.diceTwentyCB.isChecked():
            self.diceTwentyRoll = random.randint(1, 20)
        else:
            self.diceTwentyRoll = 0
            
    #Adding together all the rolls from the selected checkboxes and displaying the final roll total
        self.totalRoll = self.diceSixRoll + self.diceFourRoll + self.diceEightRoll + self.diceTenRoll + self.diceTwelveRoll + self.diceTwentyRoll + self.dicePercentRoll
        self.addLabel(text = "Your Final Roll Total is: " + str(self.totalRoll), row = 1, column = 3, background = "#e5decf")
DiceSelect().mainloop()

'''
#Project Status Report 2#
I have started this program with just trying to figure out
and get used to the GUI code while also defining the different
sets of die that can be rolled with this program. I have programmed
a simple button that rolls a D6, a regular 6-sided die.
'''
