#!/usr/bin/env python3

import itertools
import random

class Cards:

    def __init__(self): 
        self.suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs'] # Set card "suit"
        self.values = range(1, 14) # Set card "value"
        self.actual_cards = list(itertools.product(self.suits, self.values)) # Append list of "actual_cards"

    def get_card(self): # Function: Deal card
        random_number = random.randint(0, 51) # Set total number of cards to 52
        card_returned = self.actual_cards[random_number] # Create random card
        return card_returned

class Player:

    def __init__(self, ID, card):
        self.player_id = ID # Set "player_ID" number variable
        self.player_card = card # Set "player_card" value variable

class War():

    def __init__(self, number_of_players): 
        self.number_of_players = number_of_players # Set "number_of_players"
        self.player_list = [] # Create player list array

    def start_game(self):

        new_deck = Cards() # Create "new_deck" deck

        for player_id in range(0, self.number_of_players):
            player_card = new_deck.get_card() # Deal card
            new_player = Player(player_id, player_card) # Save "player_id" and "player_card" values
            self.player_list.append(new_player) # Append "new_player" values to players in "player_list" array
        
        self.decide_winner()    

    def decide_winner(self):
        winning_id = self.player_list[0] # Set player 0, as potential winner
        for player_id in self.player_list:
            if(player_id.player_card[1]>winning_id.player_card[1]): # If "player_id" higher then "winning_id"
                winning_id = player_id # Change "winning_id" to value in "player_id"
        print ("Winner is Player " + str(winning_id.player_id))
        print ("Winning Card was "+ str(winning_id.player_card[1]) + " of " + str(winning_id.player_card[0]))

def main():
    
    NewGame = War(2) # Create game, set number of players
    NewGame.start_game()

if __name__=="__main__":
    main()

