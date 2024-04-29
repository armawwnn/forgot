from nqueen import NQueensState
def hill_climbing_first_choice(start):
    current_board = start
    current_attacks = current_board.conflicts()
    steps = 0

    while True:
        neighbors = current_board.neighbors()
        next_board = None
        min_attacks = current_attacks

        for neighbor in neighbors:
            new_attacks = neighbor.conflicts()
            if new_attacks < min_attacks:
                min_attacks = new_attacks
                next_board = neighbor
                break

        if next_board is None:
            return current_board,steps
        else:
            current_board = next_board
            current_attacks = min_attacks
            steps +=1
