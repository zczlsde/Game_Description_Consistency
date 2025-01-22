from Algorithms import order_preserving_equivalence
from utils import get_payoff_matrix

def check_equivalence(reference_game, generated_game):
    
    print(order_preserving_equivalence.check_order_preserving_equivalence(reference_game, generated_game))


generated_game_path = "EFG/Setting D/GPT-4o/Imperfect Information Games/Bach or Stravinsky/Correct/1.efg"
reference_game_path = "ReferenceGame/bach.efg"

reference_game = get_payoff_matrix(reference_game_path)
generated_game = get_payoff_matrix(generated_game_path)

print(reference_game)
print(generated_game)

check_equivalence(reference_game, generated_game)



