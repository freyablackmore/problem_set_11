'''
This module provides the class CoinGame, which is useful for Q2
'''

import random

class CoinGame:
    '''
    This class represents a coin game, for which the rule of the game is as follows:
    * Start with 100 coins
    * Randomly select a player to start
    * Each player takes turn to select 1, 3 or 6 coins
    * Continue to play the game till no more coins
    * The player who got the last coin is the winner
    '''

    NUM_COIN_TO_START = 100
    
    def __init__(self, player_1, player_2):
        '''
        player_1 : Player (or any child class of Player), one of the players of the coin game
        player_2 : Player (or any child class of Player), another player of the coin game
        '''
        self._players = (player_1, player_2)

    def play(self):
        '''
        Play a round of the coin game and notify the players of the result after a game is over 
            (True for winner and False otherwise)
        return : None
        '''
        remaining_coins = CoinGame.NUM_COIN_TO_START
        player_idx = random.choice((0, 1))
        while True:
            player = self._players[player_idx]
            num_coins_selected = player.play(remaining_coins)
            assert num_coins_selected in (1, 3, 6), "number of coins selected must be 1, 3 or 6"
            remaining_coins -= num_coins_selected
            assert remaining_coins >= 0, "number of coins remaining cannot be negative"
            if remaining_coins == 0: # a player has won the game
                winner = player
                break
            player_idx = (player_idx + 1)%2 # 0 to 1 and 1 to 0
        # notify the player the game outcome
        for player in self._players:
            player.receive_outcome(player == winner)  