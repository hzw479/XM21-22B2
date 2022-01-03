from Model import nim_squared, get_winner
import Model as md
from mesa.batchrunner import BatchRunner
import pandas as pd
from functools import reduce
import operator

antal_iterationer = 100000
max_numer_of_moves = 1000


def batch_run():
    """
     Helper function.
    The function containing the batchrunner for the full simulations.
    :param
    :return: Returns
    """
    batch_run = BatchRunner(nim_squared,
                            variable_parameters={"type_of_game": [md.type_of_game]},
                            fixed_parameters={"height": md.height, "width": md.width,},
                            iterations=antal_iterationer,
                            max_steps=max_numer_of_moves,
                            model_reporters={"Winner": get_winner
                                #, "Pegs removed": lambda m: md.removed_list
                                             })



    batch_run.run_all()
    ordered_dict = batch_run.get_collector_model()
    data_list = list(ordered_dict.values()) #saves batchrunner data in list
    df = pd.concat(data_list)
    list_of_winners=[]
    for i in data_list:
        list_of_winners.append(i['Winner'].values.tolist())

    return df#reduce(operator.concat, list_of_winners)
#print("Numer of times player 1 has won the game out of", antal_iterationer, "is", batch_run().count(1))
#print(batch_run())

batch_run().to_csv(r'Mietestreadme', index = False)