# A Solution finder for the game "Calculator: The Game"

This program is designed to find solutions for the game "Calculator: The Game".
The game is a puzzle game where the player is given a number and a goal number.
The player must use a set of buttons to manipulate the given number to reach the
goal number. The buttons include addition, subtraction, multiplication, division,
and concatenation.

## How to use

At the bottom of the Python file you'll find a variable that is assigned a
6-tuple, which specifies a level of the game. Modify this tuple to match the
level, and then run the program. The program will output a list of moves that
solve the level.

```python
spec = (6,                 # num of moves
        ['+','a','-','m'], # functions available
        [3,1,2,''],        # number associated with functions
        0,                 # starting value
        123,               # goal val
        1)                 # max score
```

There are instances where a singe function is used twice, but with
different numbers. The following example shows how to handle this:

```python
spec = (2,          # num of moves
        ['+', '+'], # functions available
        [1, 2],     # number associated with functions
        0,          # starting value
        3,          # goal val
        1)          # max score
```

## The Games Functions
<!-- # add, subtract, multiply, divide, exponent, negate, remove, append, replace, reverse -->
The functions one may see as they progress in the game.

| Symbol | Function |
|--------|----------|
| +      | Addition |
| -      | Subtraction |
| *      | Multiplication |
| /      | Division |
| ^      | Exponentiation |
| f      | Negation |
| r      | Remove |
| a      | Append |
| =      | Replace |
| m      | Reverse |