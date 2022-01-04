import itertools
import numpy as np
import pickle
from ast import literal_eval as make_tuple
import random

type_of_game = 4  # 1 could be random game board each game
height = 5
width = 5
removed_list = []
file_name = 'e2a35g95'
pol1 = 'policy_p1test'
pol2 = 'policy_p2test'



class State:
    def __init__(self, p1,p2):
        self.height = height
        self.width = width
        self.board = np.array([[0,1,0,0,1],
                      [0,0,1,1,0],
                      [1,1,1,0,0],
                      [0,0,1,0,0],
                      [1,0,0,1,1]])
        self.type_of_game = type_of_game
        self.isEnd = False
        self.boardHash = None
        self.p1 = p1
        self.p2 = p2
        self.player = 1 #player 1 starts

    def getHash(self):
        self.boardHash = str(self.board.reshape(height * width))
        return self.boardHash

    def winner(self):
        peg_positions = np.argwhere(self.board==1)
        if len(peg_positions)==0:
            self.isEnd = True
            if self.player==1:
                return 1 #player 1:
            else:
                return -1 #player 2:
        else:
            self.isEnd = False
            return None

    def available_moves(self):
        moves = []
        agent_positions = np.argwhere(self.board==1)
        for i in range(width):  # moves with columns
            pegs_in_ith_column = [(x, y) for (x, y) in agent_positions if x == i]
            for j in range(len(pegs_in_ith_column) + 1):
                for subset in itertools.combinations(pegs_in_ith_column, j):
                    if subset:
                        moves.append(list(subset))
        for i in range(height):
            pegs_in_ith_row = [(x, y) for (x, y) in agent_positions if y == i]
            for j in range(len(pegs_in_ith_row) + 1):
                for subset in itertools.combinations(pegs_in_ith_row, j):
                    if subset:
                        moves.append(list(subset))
        unique_moves = []
        [unique_moves.append(x) for x in moves if x not in unique_moves]
        return unique_moves

    def change_player(self):
        if self.player ==1:
            return 2
        else:
            return 1

    def updateState(self, move):
        for i in move:
            row=i[0]
            column=i[1]
            self.board[row][column] = 0


        # only when game ends
    def giveReward(self):
        result = self.winner()
        # backpropagate reward
        if result == 1:
            self.p1.feedReward(1)
            self.p2.feedReward(0)
        elif result == -1:
            self.p1.feedReward(0)
            self.p2.feedReward(1)

    # board reset
    def reset(self):
        print(self.p1.states_value)
        self.board = np.array([[0,1,0,0,1],
                      [0,0,1,1,0],
                      [1,1,1,0,0],
                      [0,0,1,0,0],
                      [1,0,0,1,1]])
        self.boardHash = None
        self.isEnd = False
        self.player = 1

    def play(self, rounds=100):
        for i in range(rounds):
            if i % 1000 == 0:
                print("Rounds {}".format(i))
            while not self.isEnd:
                # Player 1
                positions = self.available_moves()
                p1_action = self.p1.chooseAction(positions, self.board)
                # take action and upate board state
                self.updateState(p1_action)
                board_hash = self.getHash()
                self.p1.addState(board_hash)
                # check board status if it is end

                win = self.winner()
                if win is not None:
                    # self.showBoard()
                    self.giveReward()
                    self.p1.reset()
                    self.p2.reset()
                    self.reset()
                    break

                else:
                    # Player 2
                    positions = self.available_moves()
                    p2_action = self.p2.chooseAction(positions, self.board)
                    self.updateState(p2_action)
                    board_hash = self.getHash()
                    self.p2.addState(board_hash)

                    win = self.winner()
                    if win is not None:
                        # self.showBoard()
                        # ended with p2 either win or draw
                        self.giveReward()
                        self.p1.reset()
                        self.p2.reset()
                        self.reset()
                        break

    # play with human
    def play2(self):
        while not self.isEnd:
            # Player 1
            positions = self.available_moves()
            p1_action = self.p1.chooseSmartAction(positions, self.board)
            print('Player', self.player, 'takes action', p1_action)
            # take action and upate board state
            self.updateState(p1_action)
            self.showBoard()
            # check board status if it is end
            win = self.winner()
            self.player = self.change_player()
            if win is not None:
                if win == 1:
                    print(self.p1.name, "wins!")
                    with open('readme2.txt', 'a') as f:
                        f.write('1, ')
                elif win==-1:
                    print(self.p2.name, "wins!")
                    with open('readme2.txt', 'a') as f:
                        f.write('2, ')
                self.reset()
                break

            else:
                # Player 2
                positions = self.available_moves()
                p2_action = self.p2.chooseAction(positions)
                print('Player', self.player, 'takes action', p2_action)

                self.updateState(p2_action)
                self.showBoard()
                win = self.winner()
                self.player = self.change_player()
                if win is not None:
                    if win == -1:
                        print(self.p2.name, "wins!")
                        with open('readme2.txt', 'a') as f:
                            f.write('2, ')
                    elif win == 1:
                        print(self.p1.name, "wins!")
                        with open('readme2.txt', 'a') as f:
                            f.write('1, ')
                    else:
                        print("tie!", win)
                    self.reset()
                    break

    #play with random without printing
    def play3(self):
        while not self.isEnd:
            # Player 1
            positions = self.available_moves()
            p1_action = self.p1.chooseSmartAction(positions, self.board)
            # take action and upate board state
            self.updateState(p1_action)
            #self.showBoard()
            # check board status if it is end
            win = self.winner()
            self.player = self.change_player()
            if win is not None:
                if win == 1:
                    #print(self.p1.name, "wins!")
                    with open(file_name, 'a') as f:
                        f.write('1, ')
                elif win==-1:
                    #print(self.p2.name, "wins!")
                    with open(file_name, 'a') as f:
                        f.write('2, ')
                self.reset()
                break

            else:
                # Player 2
                positions = self.available_moves()
                p2_action = self.p2.chooseAction(positions)
                self.updateState(p2_action)
                #self.showBoard()
                win = self.winner()
                self.player = self.change_player()
                if win is not None:
                    if win == -1:
                        #print(self.p2.name, "wins!")
                        with open(file_name, 'a') as f:
                            f.write('2, ')
                    elif win == 1:
                        #print(self.p1.name, "wins!")
                        with open(file_name, 'a') as f:
                            f.write('1, ')
                    else:
                        print("tie!", win)
                    self.reset()
                    break

    def showBoard(self):
        print('##########################')
        for i in range(0, height):
            print('----------------------------')
            out = '| '
            for j in range(0, width):
                if self.board[i, j] == 1:
                    token = '1'
                if self.board[i, j] == 0:
                    token = ' '
                out += token + ' | '
            print(out)
        print('----------------------------')




class Player:
    def __init__(self, name, exp_rate=0.2):
        self.name = name
        self.states = []  # record all positions taken
        self.lr = 0.35 #should decrease as you continue to gain a larger and larger knowledge base.
        self.exp_rate = exp_rate
        self.decay_gamma = 0.95 #big gamma means thinking long term
        self.states_value = {}  # state -> value

    def getHash(self, board):
        boardHash = str(board.reshape(height * width))
        return boardHash

    def chooseAction(self, positions, current_board):
        if np.random.uniform(0, 1) <= self.exp_rate:
            # take random action
            idx = np.random.choice(len(positions))
            act = positions[idx]
        else:
            value_max = -999
            for p in positions: #all possible moves
                next_board = current_board.copy()
                for i in p:
                    next_board[i] = 0 #performs a move to a fake board
                next_boardHash = self.getHash(next_board)
                value = 0 if self.states_value.get(next_boardHash) is None else self.states_value.get(next_boardHash)#checks the value for fake move
                #print("value", value)
                if value >= value_max:
                    value_max = value
                    act = p #chooses actin with highest state_value
        # print("{} takes action {}".format(self.name, action))
        return act


    def chooseSmartAction(self, positions, current_board):
            value_max = -999
            for p in positions:
                next_board = current_board.copy()
                for i in p:
                    next_board[i] = 0
                next_boardHash = self.getHash(next_board)
                value = 0 if self.states_value.get(next_boardHash) is None else self.states_value.get(next_boardHash)
                #print("value", value)
                if value >= value_max:
                    value_max = value
                    act = p
            # print("{} takes action {}".format(self.name, action))
            return act

    # append a hash state
    def addState(self, state):
        self.states.append(state)

    def feedReward(self, reward):
        for st in reversed(self.states):

            if self.states_value.get(st) is None:
                self.states_value[st] = 0
            #old_value=  self.states_value[st]
            #new_value = (1-self.lr)*old_value+self.lr*(reward+self.decay_gamma*maxV)
            self.states_value[st] += self.lr * (self.decay_gamma * reward - self.states_value[st])
            #self.states_value[st]=new_value
            reward = self.states_value[st]
            #print(st, reward)

    def reset(self):
        self.states = []

    def savePolicy(self):
        fw = open('policy_' + str(self.name)+file_name, 'wb')
        pickle.dump(self.states_value, fw)
        fw.close()

    def loadPolicy(self, file):
        fr = open(file, 'rb')
        self.states_value = pickle.load(fr)
        fr.close()


class HumanPlayer:
    def __init__(self, name):
        self.name = name

    def chooseAction(self, positions):
        while True:
            print(positions)
            action = input("Input your list of pegs to remove(without hardbrackets):")
            if len(action)<7:
                action=[make_tuple(action)]
            else:
                action=list(make_tuple(action))
            if action in positions:
                return action
            else: print('no such input')

    # append a hash state
    def addState(self, state):
        pass

    # at the end of game, backpropagate and update states value
    def feedReward(self, reward):
        pass

    def reset(self):
        pass

class RandomPlayer:
    def __init__(self, name):
        self.name = name

    def chooseAction(self, positions):
        while True:
            return random.choice(positions)

    # append a hash state
    def addState(self, state):
        pass

    # at the end of game, backpropagate and update states value
    def feedReward(self, reward):
        pass

    def reset(self):
        pass

if __name__ == "__main__":
    # training
    p1 = Player("p1")
    p2 = Player("p2")

    st = State(p1, p2)
    print("training...")
    st.play(1)
    #p1.savePolicy()
    #p2.savePolicy()
    # play with human
    #p1 = Player("computer", exp_rate=0)
    #p1.loadPolicy(pol1)
    #print(p1.states_value)
    #p2 = HumanPlayer("human")
   # p2 = RandomPlayer('Random')
   # st = State(p1, p2)
   # for i in range(100000):
   #     if i%1000==0:
   #         print('game number:', i)
   #     st.play3()
