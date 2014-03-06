#!/usr/bin/env python3

import itertools
import random

class Cards:

    def __init__(self):
        self.suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
        self.values = range(1, 14)
        self.actual_cards = []
        for card in itertools.product(self.suits,self.values):
            self.actual_cards.append(card)

    def get_card(self):
        random_number = random.randint(0, 51)
        card_returned = self.actual_cards[random_number]
        return card_returned

class Player:

    def __init__(self, ID, card):
        self.player_id = ID
        self.player_card = card

class War():

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.player_list = []

    def start_game(self):

        new_deck = Cards()

        for player_id in range(0, self.number_of_players):
            player_card = new_deck.get_card()
            new_player = Player(player_id, player_card)
            self.player_list.append(new_player)
        self.decide_winner()    

    def decide_winner(self):
        winning_id = self.player_list[0]
        for player_id in self.player_list:
            if(player_id.player_card[1]>winning_id.player_card[1]):
                winning_id = player_id
        print ("Winner is Player " + str(winning_id.player_id))
        print ("Winning Card was "+ str(winning_id.player_card[1]) + " of " + str(winning_id.player_card[0]))

def main():
    NewGame = War(2)
    NewGame.start_game()

if __name__=="__main__":
    main()
