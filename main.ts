/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Liya Getachew
 * Created on: Oct 2023
 * This program plays rock paper scissors.
*/

basic.clearScreen()
basic.showIcon(IconNames.Heart)

// variable
let rockPaperScissor: number = -1
let score: number = 0

input.onGesture(Gesture.Shake, function () {
  rockPaperScissor = randint(0, 2)
  basic.clearScreen()

  // if rockPaperScissor is 0
  if (rockPaperScissor === 0) {
    basic.showIcon(IconNames.Scissors)
  }

  // if rockPaperScissor is 1
  if (rockPaperScissor === 1) {
    basic.showLeds(`
        . . . . .
        . # # # .
        . # # # .
        . # # # .
        . . . . .
    `)
  }

  // if rockPaperScissor is 2
  if (rockPaperScissor === 2) {
    basic.showLeds(`
        # # # # #
        # . . . #
        # . . . #
        # . . . #
        # # # # #
    `)
  }

  basic.pause(5000)
  basic.showIcon(IconNames.QuarterNote)
})

input.onButtonPressed(Button.A, function () {
  score = score + 1
})

input.onButtonPressed(Button.B, function () {
  basic.clearScreen()
  basic.showString('Score : ' + score.toString())
})
