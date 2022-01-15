from mesa import Agent


class peg(Agent):
    """PEGS"""
    def __init__(self, id, model):
        super().__init__(id, model)
        self.removed = False #whether or not the peg has been taken


