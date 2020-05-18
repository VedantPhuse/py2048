# py2048

This repository contains my code for 2048 Game in command line.

Because of availibility of limited resources, i have coded and tested this in Windows only, using Visual Studio Code

You will be prompted to choose whether wou want the default game size of 5 or change it. You can enter y and then input any intiger greater than 1.

Similarly, you will be prompted to choose whether you want the wining number to be the default 2048 or change it. The winnning number will be automatically be assigned as the nearest higher power of 2. For eg, if you input 48, winning number will be 64.
Also, the game has been hardcoded to allow only the highest possible value on the board to be permitted as the winning umber.
I mean, you dont like a game which you can never win, right?

Next, you will be shown your goal, i.e. the number that you want to reach to win.

You can input your move and press enter. 
w is up
s is down
a is left of user
d is right of user

If you enter a character other than the above  mentioned ones, you will have to re-enter a valid move.

The moment winning quantity appears on the matrix,u win the game.

Similarly, if there is no scope of further movement, the game will declare you as lost.

Alternatively, you can quit the game by inputting q instead of w/a/s/d

I tested the game in Windows 10 Command Prompt

The code has been commented well so I am in confusion whether I need to copy everything and explain the working here again, totally or not.
