# PyChess


# python-chess-game
My first game written in Python and using the PyGame library. The main purpose of this game is to practice and learn game development and software engineering with PyGame.
2 Players Chess.

## Getting Started

### Prerequisites
In order to run the game or participate in its developemnts one should have the PyGame game development library. One should install it using the following command: 
```
pip install pygame
``` 

### Run
After you have downloaded and installed the pygame library, you can run the game with
```
python3.5 main.py
```

## About The Game

### Important Notes 

It is worthy to note that this version of game is incomplete. First of all, it does not have the option to castle - this will be added in next version of the game. Second, for one to win a game he must <b>eat</b> opponents king. There is still no validation of check-mate to stop the game without eating king. 
 
## Future Plans
1) Implement the alpha-beta version of minimax algorithm to increase the AI performance.
2) Implement moves database for openings and end games to increase the AI performance.
3) Code review and improvements, especially within the GameTerminal.py file.
4) Add castle moves.
5) Implement the `save log` functionality. 
6)ComputerAI.py` - Contains the `ComputerAI` class that is responsible for the computer player. Currently, the algorithm that is used is the regular minimax algorithm.

## Project Architecture

### Project Structure 
* ```Game.py``` - This file contains the main game object. The `Game` object is responsible for running and manage whole game. In our project, there is only one instance of `Game` object.  
* `Board.py`
- The logical board is controller that conrols and manipulates the board of the game. Each operation that is done and performed in game may reflect on the board and manipulate it. - Contains the `Move` class that represents each move made by user or computer on the board. 
* `Pieces.py` - Contains a  class `Pieces` that deals with logic of pieces.

## Current Version

* v1.0.0

## Built With

* [Python](https://www.python.org/) - The Python programming language.
* [pygame](https://www.pygame.org/news) - Python library for multimedia applications.

## Authors

* **Chia Yong Kang** - *Adaptation* - [ExtremelySunnyYK](https://github.com/ExtremelySunnyYK)
* **Tech with Tim** - *Initial Work* - [TechwTim](https://techwithtim.net/)
