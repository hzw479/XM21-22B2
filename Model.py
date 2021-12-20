from mesa import Agent, Model
import Agent as ac
from mesa.time import SimultaneousActivation
from mesa.space import SingleGrid
import random
from mesa.datacollection import DataCollector

type_of_game= 1 #1 could be random game board each game
height = 10
width = 10

def set_up_game(self,h,w,set_up_type):
    """ CREATES THE SETUP FOR THE GAME"""
    if set_up_type==1:
        number_of_pegs= random.randint(2,h*w) #decides number og pegs in game
        for i in range(number_of_pegs):
            peggie = ac.peg(i, self)
            self.schedule.add(peggie)
            position= self.grid.find_empty()
            self.grid.place_agent(peggie,position)

def make_move(self):
    r_or_c = random.choice(["r", "c"]) # choose whether to pick a row or column
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
    for p in chosen_pegs:
        agent_to_remove = self.grid.get_cell_list_contents(p)[0]
        self.grid.remove_agent(agent_to_remove)
        self.schedule.remove(agent_to_remove)

def get_winner(self):
    return self.winner

class nim_squared(Model):
    def __init__(self, height, width, type_of_game):
        self.height=height
        self.width = width
        self.type_of_game = type_of_game
        self.grid = SingleGrid(width, height, torus=False)  # torus wraps edges
        self.schedule = SimultaneousActivation(self)
        self.player = 1
        self.winner = 0
        self.datacollector = DataCollector(model_reporters={"Winner": lambda m: get_winner(m)
                                                            })

        set_up_game(self, height, width, type_of_game)
        self.running = True
    def step(self):
        if len(self.schedule.agents)>1:
            self.schedule.step()
            make_move(self)
            if len(self.schedule.agents)==0:
                #print("Winner is player", self.player)
                self.winner=self.player
                self.datacollector.collect(self)
                self.running = False
                return self.winner
        elif len(self.schedule.agents)==1:
            #print("Winner is player", self.player)
            self.winner=self.player
            self.datacollector.collect(self)
            self.running = False
            return self.winner

        self.player = 1 + ((self.player) % 2)




        #self.datacollector.collect(self)



