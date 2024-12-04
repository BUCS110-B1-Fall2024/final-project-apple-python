
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

![final gui](assets/finalgui.jpg)

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


## ATP

| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Click Quit Button    |Program closes                     |
|  2                   | Click Start Button   | State loop changes to mainmap, mainmap pops up |
|  3                   | Within Main Map, Click Hinman Button| A Picture of Hinman pops up, along with info Buttons|
|  4                   | Within Main Map, Click Quit button in top right corner | User is taken back to start screen |
|  5                   | Within Hinman,click info Button | On the lower 4th of the screen, information about Hinman College displays |
