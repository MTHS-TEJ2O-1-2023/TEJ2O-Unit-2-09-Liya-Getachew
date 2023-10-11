"""
Created by: Liya Getachew
Created on: Oct 2023
This module is a Micro:bit MicroPython program that plays rock paper scissors.
"""

from microbit import *
from random import *


display.clear()
display.show(Image.HEART)

# variables
rock_paper_scissors = -1
score = 0
scissor = Image("88008:88080:00800:88080:88008")
rock = Image("00000:08880:08880:08880:00000")
paper = Image("88888:80008:80008:80008:88888")

while True:
    gesture = accelerometer.current_gesture()
    if gesture == "shake":
        # pick a number from 0 to 2
        rock_paper_scissors = randint(0, 2)
        display.clear()

        # if rock_paper_scissor is 0
        if rock_paper_scissors == 0:
            display.show(scissor)

        # if rock_paper_scissor is 1
        if rock_paper_scissors == 1:
            display.show(rock)

        # if rock_paper_scissor is 2
        if rock_paper_scissors == 2:
            display.show(paper)

        sleep(5000)
        display.show(Image.HEART)

    if button_a.is_pressed():
        score = score + 1
    if button_b.is_pressed():
        display.scroll("Score : " + str(score))
