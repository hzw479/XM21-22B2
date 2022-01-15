from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from ABM import Model as md
from ABM.Model import nim_squared



def draw_pegs(agent):
    """function to display pegs"""
    if agent.removed == False:
        portrayal = {"Shape": "rect",
                     "Color": "black",
                     "w": 0.9, "h":0.9,
                     "Filled": "true",
                     "Layer": 0,
        }

    return portrayal


grid = CanvasGrid(draw_pegs, md.width, md.height, 1000, 900)

server = ModularServer(nim_squared, [grid],
"Peg Model",
{"height":md.height, "width":md.width,"type_of_game": md.type_of_game})
server.port = 8521 # The default