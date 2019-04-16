#!/usr/bin/env python3

# This program plays a game of Rock, Paper, Scissors

import random


moves = ['rock', 'paper', 'scissors']


# This class is the parent class for all of the Players

class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


# Function that defines the winners

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


# This class is the parent class for the game in self

class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_pts = 0
        self.p2_pts = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            print("PLAYER 1 WON!")
            self.p1_pts += 1
        elif beats(move2, move1):
            print("PLAYER 2 WON!")
            self.p2_pts += 1
        else:
            print("TIE!!")

        print(f"Player ONE {self.p1_pts} x {self.p2_pts} Player TWO")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")

        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


# Random Player

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# Human Player Class

class HumanPlayer(Player):
    def move(self):
        check = False
        while check is False:
            human_move = input("Choose one: Scissors, Paper or Rock. ").lower()

            # Testing if is a possible choice move
            if human_move not in moves:
                print("Please write a valid move.")
            else:
                check = True
                return human_move


# Reflect Player who plays the same move as the human did in last round

class ReflectPlayer(Player):

    def __init__(self):
        self.reflectedplayer_move = []
        self.reflectplayer_move = []

    # Always plays the Human Player except in the 1st round that plays randomly
    def move(self):
        if self.reflectedplayer_move == []:
            return random.choice(moves)
        else:
            return self.reflectedplayer_move[-1]

    # append moves to lists
    def learn(self, my_move, their_move):
        self.reflectplayer_move.append(my_move)
        self.reflectedplayer_move.append(their_move)


# Cycle Player class never repeat the same move

class CyclePlayer(Player):
    def __init__(self):
        self.cycleplayer_move = ""
        self.index = 0

    def move(self):
        if self.cycleplayer_move == "":
            self.index = random.randint(0, 2)
            self.cycleplayer_move = moves[self.index]
            if self.index == 2:
                self.index = 0
            else:
                self.index += 1
            return self.cycleplayer_move
        elif self.cycleplayer_move == moves[2]:
            self.index = 1
            self.cycleplayer_move = moves[0]
            return self.cycleplayer_move
        else:
            self.cycleplayer_move = moves[self.index]
            self.index += 1
            return self.cycleplayer_move


players = [RandomPlayer(), ReflectPlayer(), CyclePlayer()]


# Welcome message and opponets choice

def start():

    print("Welcome to Rock-Paper-Scissors Game!\n\n")
    print("Choose your opponent by pressing the corresponding number. ")
    print("[1] Random Player\n[2] Reflect Player\n[3] Cycle Player\n")
    check = False
    index = ""
    while check is False:
        index = int(input("Choose a number then press ENTER/RETURN: "))
        if players[index - 1] not in players:
            print("Please enter a valid number.")
        else:
            check = True
    rival = players[index - 1]
    return rival


if __name__ == '__main__':

    # Running the game
    game = Game(HumanPlayer(), start())
    game.play_game()
