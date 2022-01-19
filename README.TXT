
This repository consists on 2 directories of interest.

ABM:
ABM stands for Agent Based Model, and this directory contains files regarding this model.
    Agent.py contains the class which holds the pegs. As pegs cannot do anything, this file contains nothing of
    real interest and is purely there for the program to work. Note you do not have to run this file.

    Model.py contains the game itself. This is the nim_squared class. The class is initialized with model specific
    parameters as well as a step function. The step function is what actually plays the game. The step function
    works simply by first calling a make_move function and then changing the player afterwards. This file
    contains a few more functions which are there for the program to work, but these are well commented within
    the file. The function _make_move is not in use as it was made in the progress of finding the most efficient
    way of choosing moves. In the top of the file, 4 parameters are defined. If the user wish to play a game
    with a random game board, change the value of type_of_game to 1 and the values of height and width to the
    dimensions desired. Is the user wish to play a costumized board let type_of_game equal 2 and alter
    peg_placings at line 25 to a list consisting of the desired peg placements. Note you still have to state
    the right dimensions regarding height and width. Note the you do not have to run this file.

    Visualization.py contains all that is used for visualizing the game. It contains a function which defines
    color an size for the pegs. It also chooses the (physical) size of the grid. Do not alter this file.
    Note you do not have to run this file.

    run.py is the file which launches the server and thus starts the game. Do not alter this file. THIS IS THE
    ONLY FILE TO RUN WHEN WANTING TO PLAY.

    Batchrunner.py contains a function which is able to play the game for an indefinite number of times. It
    collects data for all of these games and returns it as a data frame. The end of the file runs the function
    at exports the data frame as a csv file. There are three parameters at the top of the file. Do not alter
    max_numer_of_moves as this is just a bound. antal_iterationer can be altered to choose how many games the
    function should collect data for, and name_of_csv_to_create can be altered to choose the desired name for
    the csv file to export. This is the only file you need to run for collecting data.
    Note that playing the game this way will not be visualized in any way.

RL:
RL stands for Reinforcement Learning. This directory contains a file containing the deep learning model as well
as a directory containing all policy files from the model.
    DeepLearning.py is the model running the game and training the player. Line 10,11,12 allows you to name the
    file consisting of game data, i.e. list of moves as well as winning player, and also name the player policies
    for this game. The game is played with a set game board, which is defined on line 20. If you wich another
    game board, this is where you should alter. If you wish to change the hyper parameters for Player 1, this is
    done on line 286 (epsilon), line 289 (learning rate) and line 291 (gamma).
    To play the game, scroll to line 453. Line 460 allows you to choose the number of training games. If you
    uncomment line 464 to 470 and comment out line 472 to line 479 the program will first train the agent and then
    afterwards initialize a game where you are player two. This allows you to play against the trained agent. You
    will be showed the game board as well as a list of possible moves. You then write which pegs you would like to
    remove. This needs to be on the form (x,y), (z,w) and so on.
    If you keep line 472 to line 479 uncommented, and line 464 to line 470 commented out, the program will first
    train the player and then afterwards play against a random player. The number of games to be played against
    the random player can be altered at line 476.


The repository also contains a parsing file where you on line 4 and line 5 write the names of two csv files, one consisting
of data from a so called smart game, and the other consisting of data for games consisting of random moves. Running the file
calculates the percentages of wins of player 1 for each of the files.

