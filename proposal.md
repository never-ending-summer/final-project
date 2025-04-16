# MyPalette

## Repository
[<Public GitHub respository>](https://github.com/never-ending-summer/final-project)

## Description
MyPalette would be a color palette generator for digital artists. It randomely picks 5 colors and puts out an image showcasing them alongside each other, with the hex codes as well

## Features
- Picking Colors
	- By using random module to pick the r, g and b from 0 to 255
- Turn numbers to Displayable Hex Code
	- By using hex() function, it can convert the previously randomized output into a proper hex code
- Create image of Palette
	- Taking the first feature, colors, and the second feature, hex codes, they are combined into an image that can be saved

## Challenges
- How to place each color into the image in the correct spot, maybe return and review the previous lesson on image modification
- How to generate palette that matches with color theory
- Look more into PIL, which will be used for this project

## Outcomes
Ideal Outcome:
- The program generates 5 random colors, and is able to create the hex code. Both will appear on the image generated. This should be able to be saved to your computer

Minimal Viable Outcome:
- It can at least show the 5 different colors picked on the screen. It could show just the hex codes, but it isn't as easy for the artist to check to see how coherent it is and if it looks like it would work on their (website, poster, etc)

## Milestones

- Week 1
  1. Start research. Look into the library(or libraries) that will be used for the code
  2. Once done with that, move onto beginning writing the code. Start with the first step, picking colors

- Week 2
  1. Finish picking colors, work on hex code conversion
  2. Start practicing/research image generating based on what we have

- Week N (Final)
  1. Review what has been completed so far, and make sure the code works properly (with/without image generation)
  2. Complete code
