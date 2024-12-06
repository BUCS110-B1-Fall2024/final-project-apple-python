
:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# Apple Python
## CS110 B1 Final Project  Fall, 2024

## Team Members

Allison Jenkins, Jessie Kaufman

***

## Project Description

Our project will take the user on a tour of the Binghamton campus. It will include pictures of the different places, and extra information about the buildings.

***    

## GUI Design

### Initial Design

(assests/College_Tour.jpg)

### Final Design

(assets\main_gui.png)
(assets\ciw_gui.png)

## Program Design

### Features

1. A Start Screen
2. An Overall Map Where You Can Choose Where To Go
3. A Back Button 
4. A Quit Feature To go Back To Start Screen
5. Different Information Screens For Each Place

### Classes

Class Buttons: makes buttons depending on a given input
Class Images: Allows images to be displayed
Class Controller: Defines the game controller
Class Info: Stores the place information, and allows it to be displayed on screen


## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Click Quit Button    |Program closes                     |
|  2                   | Click Start Button   | State loop changes to mainmap, mainmap pops up |
|  3                   | Within Main Map, Click Hinman Button| A Picture of Hinman pops up, along with info button|
|  4                   | Within Hinman, Click Info Button | On the lower 4th of the screen, information about Hinman College displays |
|  5                   | Within Hinman, Click Quit Button | User is taken back to main map |
|  6                   | Within Main Map, Click Quit Button in Top Right Corner | User is taken back to start screen |