from mesa import Model
from ABM import Agent as ac
from mesa.time import SimultaneousActivation
from mesa.space import SingleGrid
import random
from mesa.datacollection import DataCollector
from scipy.special import comb
import itertools

type_of_game= 2 #1 could be random game board each game
height = 5
width = 5
removed_list = []

def set_up_game(self,h,w,set_up_type):
    """ CREATES THE SETUP FOR THE GAME"""
    if set_up_type==1:
        number_of_pegs= random.randint(2,h*w) #decides number og pegs in game
        for i in range(number_of_pegs):
            peggie = ac.peg(i, self)
            self.schedule.add(peggie)
            position= self.grid.find_empty()
            self.grid.place_agent(peggie,position)
    elif set_up_type==2: #Mie
        #peg_placings=[(0,2),(1,1),(1,2), (1,4), (2,4), (3,0),(3,2), (4,1), (4,4)] #hw5
        #peg_placings = [(0,1),(0,2), (1,0),(2,2)] #hw3
        #peg_placings = [(i,j) for i in range(4) for j in range(4)]
        peg_placings = [(0,2), (1,2), (1,4), (2,1), (2,2), (2,3),(4,4),(3,3),]
        #removed_pegs=[(3,3),(3,0),(0,0), ]
        for i in range(len(peg_placings)):
            peggie = ac.peg(i,self)
            self.schedule.add(peggie)
            position = peg_placings[i]
            self.grid.place_agent(peggie, position)
    elif set_up_type==3: #Mette h3, w4
        #peg_placings=[(0,1),(0,2),(1,0),(1,2),(2,0),(2,1), (3,0), (3,2)]
        peg_placings = [(0,1),(1,1),(1,2),(2,1), (1,0), (2,2), (3,0), (3,1)]
        for i in range(len(peg_placings)):
            peggie = ac.peg(i,self)
            self.schedule.add(peggie)
            position = peg_placings[i]
            self.grid.place_agent(peggie, position)
    elif set_up_type==4: #Diana h4, w4
        #peg_placings=[(0,1), (0,2), (1,0), (1,3), (2,2), (3,0)]
        #peg_placings = [(0,0), (0,2), (1,3), (2,0), (2,2), (3,1), (3,3)]
        peg_placings = [(0,0),(0,2),(0,4),(2,1),(2,2),(2,3),(3,4),(4,0),(4,2),(4,3)]
        for i in range(len(peg_placings)):
            peggie = ac.peg(i,self)
            self.schedule.add(peggie)
            position = peg_placings[i]
            self.grid.place_agent(peggie, position)
def number_of_moves(self):
    agent_count = len([a for a in self.schedule.agents])
    agent_positions = [a.pos for a in self.schedule.agents]
    list_of_rows = []
    list_of_columns=[]
    for i in range(height):
        temp = 0
        for j in agent_positions:
            if j[1]==i:
                temp+=1
        list_of_rows.append(temp)
    for i in range(width):
        temp = 0
        for j in agent_positions:
            if j[0]==i:
                temp+=1
        list_of_columns.append(temp)
    total_sum=agent_count
    for i in list_of_rows:
        if i>1:
            for j in range(2,i+1):
                total_sum+=comb(i,j)
    for i in list_of_columns:
        if i>1:
            for j in range(2,i+1):
                total_sum+=comb(i,j)
    return total_sum

def make_move(self):
    agent_positions = [a.pos for a in self.schedule.agents]
    X = set([x for (x, y) in agent_positions])
    Y = set([y for (x, y) in agent_positions])
    if len(X) == 1 or len(Y) == 1:
        self.winner = self.player
        agent_positions = [a.pos for a in self.schedule.agents]
        temp_list = []
        for p in agent_positions:
            agent_to_remove = self.grid.get_cell_list_contents(p)[0]
            self.grid.remove_agent(agent_to_remove)
            self.schedule.remove(agent_to_remove)
            temp_list.append(p)
        self.removed_list.append(temp_list)
        self.datacollector.collect(self)
        self.running = False
        self.removed_list = []


    else:
        possible_moves = get_list_of_possible_moves(self)
        chosen_pegs = random.choice(possible_moves)
        temp_list = []
        for p in chosen_pegs:
            agent_to_remove = self.grid.get_cell_list_contents(p)[0]
            self.grid.remove_agent(agent_to_remove)
            self.schedule.remove(agent_to_remove)
            temp_list.append(p)
        self.removed_list.append(temp_list)
def _make_move(self):
    agent_positions = [a.pos for a in self.schedule.agents]
    X = set([x for (x,y) in agent_positions])
    Y = set([y for (x,y) in agent_positions])
    if len(X) == 1 or len(Y) == 1:
        self.winner = self.player
        agent_positions = [a.pos for a in self.schedule.agents]
        temp_list=[]
        for p in agent_positions:
            agent_to_remove = self.grid.get_cell_list_contents(p)[0]
            self.grid.remove_agent(agent_to_remove)
            self.schedule.remove(agent_to_remove)
            temp_list.append(p)
        self.removed_list.append(temp_list)
        self.datacollector.collect(self)
        self.running = False
        self.removed_list = []


    else:

        r_or_c = random.choice(["r", "c"])  # choose whether to pick a row or column
        if r_or_c == "r":
            possible_rows=[i for i in range(0,height)]
            random.shuffle(possible_rows)
            which_r = possible_rows.pop()
            possible_indicies = [(x,which_r) for x in range(width)]
            while len(self.grid.get_cell_list_contents(possible_indicies))==0:#if row is empty
                which_r = possible_rows.pop()
                possible_indicies = [(x, which_r) for x in range(width)]
            possible_pegs_to_take =[]
            for i in possible_indicies:
                if not self.grid.is_cell_empty(i): #checks whether a peg is present
                    possible_pegs_to_take.append(i)
            chosen_pegs=[]
            number_of_pegs_to_choose = random.randint(1,len(possible_pegs_to_take))
            for i in range(number_of_pegs_to_choose):
                choice = random.choice(possible_pegs_to_take)
                chosen_pegs.append(choice)
                possible_pegs_to_take.remove(choice)
            if len(chosen_pegs)==0:
                chosen_pegs.append(random.choice(possible_pegs_to_take))
        else:
            possible_columns = [i for i in range(0,width)]
            random.shuffle(possible_columns)
            which_c = possible_columns.pop()
            possible_indicies = [(which_c,y) for y in range(height)]
            while len(self.grid.get_cell_list_contents(possible_indicies))==0:#if column is empty
                which_c = possible_columns.pop()
                possible_indicies = [(which_c,y) for y in range(height)]
            possible_pegs_to_take = []
            for i in possible_indicies:
                if not self.grid.is_cell_empty(i):
                    possible_pegs_to_take.append(i)
            chosen_pegs = []
            number_of_pegs_to_choose = random.randint(1, len(possible_pegs_to_take))
            for i in range(number_of_pegs_to_choose):
                choice = random.choice(possible_pegs_to_take)
                chosen_pegs.append(choice)
                possible_pegs_to_take.remove(choice)
            if len(chosen_pegs) == 0:
                chosen_pegs.append(random.choice(possible_pegs_to_take))

        temp_list=[]
        for p in chosen_pegs:
            agent_to_remove = self.grid.get_cell_list_contents(p)[0]
            self.grid.remove_agent(agent_to_remove)
            self.schedule.remove(agent_to_remove)
            temp_list.append(p)
        self.removed_list.append(temp_list)

def get_winner(self):
    return self.winner

def get_list_of_possible_moves(self):
    moves=[]
    agent_positions = [a.pos for a in self.schedule.agents]
    for i in range(width): #moves with columns
        pegs_in_ith_column = [(x,y) for (x,y) in agent_positions if x== i]
        for j in range(len(pegs_in_ith_column)+1):
            for subset in itertools.combinations(pegs_in_ith_column, j):
                if subset:
                    moves.append(list(subset))
    for i in range(height):
        pegs_in_ith_row = [(x, y) for (x, y) in agent_positions if y == i]
        for j in range(len(pegs_in_ith_row) + 1):
            for subset in itertools.combinations(pegs_in_ith_row, j):
                if subset:
                    moves.append(list(subset))
        unique_moves=[]
        [unique_moves.append(x) for x in moves if x not in unique_moves]
        return unique_moves
class nim_squared(Model):
    def __init__(self, height, width, type_of_game):
        self.height=height
        self.width = width
        self.type_of_game = type_of_game
        self.grid = SingleGrid(width, height, torus=False)  # torus wraps edges
        self.schedule = SimultaneousActivation(self)
        self.player = 1
        self.winner = 0
        self.datacollector = DataCollector(model_reporters={"Winner": lambda m: get_winner(m),
                                                            "Pegs removed": lambda  m: self.removed_list
                                                            })
        self.removed_list = []
        set_up_game(self, height, width, type_of_game)
        self.running = True
        self.timer=0
    def step(self):
        self.schedule.step()
        make_move(self)
        get_list_of_possible_moves(self)
        self.player = 1 + ((self.player) % 2)











