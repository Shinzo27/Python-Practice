import random

def select_winner():

    winner_token_id = random.randint(1, 600)
    return winner_token_id

winner_token_id = select_winner()

print("The winner of the lucky draw is the parent with token ID:", winner_token_id)
