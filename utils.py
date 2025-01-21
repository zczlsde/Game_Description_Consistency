import pygambit as gbt
import numpy as np

def get_payoff_matrix(efg_file_path):
    efg = gbt.Game.read_game(efg_file_path)
    nfg_str = efg.write(fromat='nfg')
    nfg = gbt.Game.parse_game(nfg_str)
    payoff_gambit = nfg.to_arrays()
    
    payoff = []
    number_of_players = 2 # TODO: generalize for n players
    for i in range(number_of_players):
        payoff.append(payoff_gambit[i].astype(float))
    
    print(payoff)
    return payoff


get_payoff_matrix('/home/samuel/Dataset/Game_Description_Consistency/1.efg')