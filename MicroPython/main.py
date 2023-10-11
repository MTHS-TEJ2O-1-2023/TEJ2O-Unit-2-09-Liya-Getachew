"""
Created by: Liya Getachew
Created on: Oct 2023
This module is a Micro:bit MicroPython program that plays rock paper scissors.
"""

from microbit import *


display.clear()
display.show(Image.HEART)

# variables 
rock_paper_scissors = -1
score = 0

while True:
    if button_a.is_pressed():
        score = score + 1
    if button_b.is_pressed():
        display.scroll("Score : " + str(score))

