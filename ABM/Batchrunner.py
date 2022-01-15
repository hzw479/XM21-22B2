from Model import nim_squared, get_winner
import Model as md
from mesa.batchrunner import BatchRunner
import pandas as pd


antal_iterationer = 100000
max_numer_of_moves = 1000
name_of_csv_to_create = 'random100k'

def batch_run():
    """
     This function runs the simulation a number of times without visualization.
    :param
    :return: Returns a data frame consisting of data from the simulations to be converted to a csv file
    """
    batch_run = BatchRunner(nim_squared,
                            variable_parameters={"type_of_game": [md.type_of_game]},
                            fixed_parameters={"height": md.height, "width": md.width,},
                            iterations=antal_iterationer,
                            max_steps=max_numer_of_moves,
                            model_reporters={"Winner": get_winner
                                             })
    batch_run.run_all()
    ordered_dict = batch_run.get_collector_model()
    data_list = list(ordered_dict.values()) #saves batchrunner data in list
    df = pd.concat(data_list)
    list_of_winners=[]
    for i in data_list:
        list_of_winners.append(i['Winner'].values.tolist())

    return df

batch_run().to_csv(name_of_csv_to_create, index = False)