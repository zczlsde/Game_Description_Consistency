import numpy as np


def get_relationship(x, y):
    """
    Determine the relationship R(x, y).

    Args:
        x: First value.
        y: Second value.

    Returns:
        A string representing the relationship: ">", "<", or "=".
    """
    if x > y:
        return ">"
    elif x < y:
        return "<"
    else:
        return "="


def check_order_preserving_equivalence(payoff_matrix_g, payoff_matrix_g_prime):
    """
    Check whether two games are order-preserving equivalent.

    Args:
        payoff_matrix_g: A list of numpy arrays representing the payoff matrices for each player in game G.
        payoff_matrix_g_prime: A list of numpy arrays representing the payoff matrices for each player in game G'.

    Returns:
        True if the games are order-preserving equivalent, False otherwise.
    """
    num_players = len(payoff_matrix_g)

    for player in range(num_players):
        num_strategies = payoff_matrix_g[player].shape[0]
        num_opponent_strategies = payoff_matrix_g[player].shape[1]

        for s_i in range(num_strategies):
            for s_i_prime in range(num_strategies):
                if s_i == s_i_prime:
                    continue

                for s_minus_i in range(num_opponent_strategies):
                    # Payoffs in game G
                    u_g = payoff_matrix_g[player][s_i, s_minus_i]
                    u_g_prime = payoff_matrix_g[player][s_i_prime, s_minus_i]

                    # Payoffs in game G'
                    u_g_dash = payoff_matrix_g_prime[player][s_i, s_minus_i]
                    u_g_prime_dash = payoff_matrix_g_prime[player][s_i_prime, s_minus_i]

                    # Compare relationships
                    relation_g = get_relationship(u_g, u_g_prime)
                    relation_g_prime = get_relationship(u_g_dash, u_g_prime_dash)

                    if relation_g != relation_g_prime:
                        return False  # Relation mismatch found

    return True


# Example usage
if __name__ == "__main__":
    # Payoff matrices for a 2-player game (row player and column player)
    # Each player has 2 strategies
    payoff_matrix_g = [
        np.array([[3, 0], [5, 1]]),  # Payoffs for player 1
        np.array([[2, 4], [0, 6]])  # Payoffs for player 2
    ]

    payoff_matrix_g_prime = [
        np.array([[6, 0], [10, 2]]),  # Payoffs for player 1
        np.array([[8, 12], [1, 15]])  # Payoffs for player 2
    ]

    print("Are the games order-preserving equivalent?")
    print(check_order_preserving_equivalence(payoff_matrix_g, payoff_matrix_g_prime))
